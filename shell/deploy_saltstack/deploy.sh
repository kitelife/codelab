#!/bin/sh

target_ip=$1

scp -r -P 22 /inner-warehouse-monitor/* root@$target_ip:/usr/local/inner-warehouse-monitor/
scp -r -P 22 /srv/* root@$target_ip:/srv/
scp -P 22 CentOS-Base.repo root@$target_ip:/etc/yum.repos.d/CentOS-Base.repo
scp -P 22 install.sh root@$target_ip:/root/

/usr/bin/ssh -n -p 22 root@$target_ip "mv /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.bak"
/usr/bin/ssh -n -p 22 root@$target_ip "yum -y install ntp"
/usr/bin/ssh -n -p 22 root@$target_ip "ntpdate 192.168.2.33 && hwclock -w"
/usr/bin/ssh -n -p 22 root@$target_ip "chmod +x /root/install.sh && /root/install.sh"
