#!/bin/sh

function stop_iptables()
{
    service iptables stop
    chkconfig iptables off
    service ip6tables stop
    chkconfig ip6tables off
}

function master_entry()
{

    stop_iptables

    echo "If run HAProxy, please input 1"
    echo "If run HAProxyConsole, please input 2"
    echo "If run Keepalived, please input 3"
    echo "If run BIND, please input 4"
    echo "If run all(HAProxy, HAProxyConsole, Keepalived, BIND), please input 0"
    echo -n ": "
    read line
    case $line in
        1)
            service rsyslog restart
            /usr/local/haproxy/sbin/haproxy -f /usr/local/haproxy/conf/haproxy.conf &
            echo "*** Run HAproxy successfully! ***"
            ;;
        2)
            cd /usr/local/haproxyconsole/bin && ./haproxyconsole &
            echo "*** Run HAproxyConsole successfully! ***"
            ;;
        3)
            /usr/local/keepalived/sbin/keepalived -P -D -S 4 -D
            echo "*** Run Keepalived successfully! ***"
            ;;
        4)
            /usr/local/bind9.9.3/sbin/named &
            echo "*** Run BIND successfully! ***"
            ;;
        0)
            /usr/local/haproxy/sbin/haproxy -f /usr/local/haproxy/conf/haproxy.conf &
            cd /usr/local/haproxyconsole/bin && ./haproxyconsole &
            /usr/local/keepalived/sbin/keepalived -P -D -S 4 -D
            /usr/local/bind9.9.3/sbin/named &
            echo "*** Run all(HAProxy, HAProxyConsole, Keepalived, BIND) successfully! ***"
            ;;
        *)
            echo "Error, No Such Option!"
    esac
	
}

function slave_entry()
{

    stop_iptables

    echo "If run HAProxy, please input 1"
    echo "If run Keepalived, please input 2"
    echo "If run BIND, please input 3"
    echo "If run all(HAProxy, Keepalived, BIND), please input 0"
    echo -n ": "
    read line
    case $line in
        1)
            service rsyslog restart
            /usr/local/haproxy/sbin/haproxy -f /usr/local/haproxy/conf/haproxy.conf &
            echo "*** Run HAproxy successfully! ***"
            ;;
        2)
            /usr/local/keepalived/sbin/keepalived -P -D -S 4 -D
            echo "*** Run Keepalived successfully! ***"
            ;;
        3)
            /usr/local/bind9.9.3/sbin/named &
            echo "*** Run BIND successfully! ***"
            ;;
        0)
            /usr/local/haproxy/sbin/haproxy -f /usr/local/haproxy/conf/haproxy.conf &
            /usr/local/keepalived/sbin/keepalived -P -D -S 4 -D
            /usr/local/bind9.9.3/sbin/named &
            echo "*** Run all(HAProxy, Keepalived, BIND) successfully! ***"
            ;;
        *)
            echo "Error, No Such Option!"
    esac
}

function usage()
{
    echo "Usage: $1 master|slave"
}

function tips_for_test()
{
cat << EOF

After running successfully, you should test to ensure that:
   HAProxy: netstat -tlnp | grep haproxy
   Keepalived: ip a  # to ensure bind vip to network card successfully
               tcpdump vrrp  # to observe the date of vrrp protocol
   BIND: /usr/local/bind9.9.3/bin/dig @127.0.0.1 www.baidu.com A
On the master server, you also should check HAProxyConsole: 
   netstat -tlnp | grep haproxyconsole
   Open the web page: http://192.168.2.193:9090 (Replace "192.168.2.193" to the ip of your server, and "9090" is the default port of HAProxyConsole)

EOF
}

function main()
{
    if [ $# = 1 ];then
        if [ "$1" = "master" ];then
            master_entry
            tips_for_test
        elif [ "$1" = "slave" ];then
            slave_entry
            tips_for_test
        else
            usage $0
            exit 1
        fi
    else
        usage $0
        exit 1
    fi 
}

main $@
