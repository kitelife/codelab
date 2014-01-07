#!/bin/sh

function deploy_haproxy()
{
    echo "*** Start to deploy HAProxy ***"
    tar -xvf HAProxy.tar.gz
    cp -r ./HAProxy/haproxy /usr/local/
    cp ./HAProxy/haproxy.logrotate /etc/logrotate.d/
    chmod +x /usr/local/haproxy/restart_haproxy.sh
    chmod +x /usr/local/haproxy/sbin/*
    echo "*** Deploy HAProxy successfully! ***"
}

function deploy_haproxyconsole()
{
    echo "*** Start to deploy HAProxyConsole ***"
    tar -xvf HAProxyConsole.tar.gz
    cp -r ./HAProxyConsole/haproxyconsole /usr/local/
    chmod +x /usr/local/haproxyconsole/bin/haproxyconsole
    echo "*** Deploy HAProxyConsole successfully! ***"
}

function deploy_keepalived()
{
    echo "*** Start to deploy Keepalived ***"
    tar -xvf Keepalived.tar.gz
    cp -r ./Keepalived/keepalived /usr/local/
    chmod +x /usr/local/keepalived/bin/*
    chmod +x /usr/local/keepalived/sbin/*
    cp -r ./Keepalived/openssl /usr/local/
    chmod +x /usr/local/openssl/bin/*
    mkdir /etc/keepalived
    if [ "$1" = "master" ];then 
        cp ./Keepalived/keepalived_master.conf /etc/keepalived/keepalived.conf
    else
        cp ./Keepalived/keepalived_slave.conf /etc/keepalived/keepalived.conf
    fi
    cp ./Keepalived/Mailnotify.py /etc/keepalived/
    chmod +x /etc/keepalived/Mailnotify.py
    echo "*** Deploy Keepalived successfully! ***"
}

function deploy_bind()
{
    echo "*** Start to deploy BIND ***"
    tar -xvf BIND.tar.gz
    cp -r ./BIND/bind9.9.3 /usr/local/
    chmod +x /usr/local/bind9.9.3/bin/*
    chmod +x /usr/local/bind9.9.3/sbin/*
    if [ "$1" = "master" ];then
        mkdir -p /usr/local/bind9.9.3/data/master
        cp ./BIND/named_master.conf /usr/local/bind9.9.3/etc/named.conf
    else
        mkdir -p /usr/local/bind9.9.3/data/slaves
        cp ./BIND/named_slave.conf /usr/local/bind9.9.3/etc/named.conf
    fi
    echo "*** Deploy BIND successfully! ***"
}

function deploy_all()
{
    deploy_haproxy
    if [ "$1" = "master" ];then
    	deploy_haproxyconsole
    fi
    deploy_keepalived $1
    deploy_bind $1
}

function usage()
{
    echo "Usage: $1 master|slave"
}

function master_entry()
{
    echo "If install HAProxy, please input 1"
    echo "If install HAProxyConsole, please input 2"
    echo "If install Keepalived, please input 3"
    echo "If install BIND, please input 4"
    echo "If install all(HAProxy, HAProxyConsole, Keepalived, BIND), please input 0"
    echo -n ": "
    read line
    case $line in
        1)
            deploy_haproxy
            ;;
        2)
            deploy_haproxyconsole
            ;;
        3)
            deploy_keepalived master
            ;;
        4)
            deploy_bind master
            ;;
        0)
            deploy_all master
            ;;
        *)
            echo "Input Error, No such option"
            ;;
    esac
}

function slave_entry()
{
    echo "If install HAProxy, please input 1"
    echo "If install Keepalived, please input 2"
    echo "If install BIND, please input 3"
    echo "If install all(HAProxy, Keepalived, BIND), please input 0"
    echo -n ": "
    read line
    case $line in
        1)
            deploy_haproxy
            ;;
        2)
            deploy_keepalived slave
            ;;
        3)
            deploy_bind slave
            ;;
        0)
            deploy_all slave
            ;;
        *)
            echo "Input Error, No such option"
            ;;
   esac
}

function deploy_tool()
{
    cp ./tcpdump /usr/sbin/
    chmod +x /usr/sbin/tcpdump
}

function tips_to_config()
{
cat << EOF

Before to execute run.sh, you should modify the file list below:
    HAProxy: /etc/rsyslog.conf
    Keepalived: /etc/keepalived/keepalived.conf, /etc/keepalived/Mailnofity.py
    BIND: /usr/local/bind9.9.3/etc/named.conf

On the master server, you also should modify the file:
    /usr/local/haproxyconsole/conf/app_conf.ini

EOF
}

function main()
{
    if [ $# = 1 ];then
        if [ "$1" = "master" ];then
            deploy_tool
            master_entry
            tips_to_config
        elif [ "$1" = "slave" ];then
            deploy_tool
	    slave_entry
            tips_to_config
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
