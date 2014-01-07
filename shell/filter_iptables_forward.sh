#!/bin/sh

while read line
do
    iptables -L FORWARD > $1
    awk -v ip="$line" 'NR > 2 && $5 == ip { print $5, $7 }' $1 | uniq -f 2 -c
done<target_ip_list.txt
