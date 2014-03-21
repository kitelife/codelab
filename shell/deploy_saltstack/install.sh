#!/bin/sh

# scp -r -P 22 /inner-warehouse-monitor/ root@target_ip:/usr/local/inner-warehouse-monitor/
# scp -r -P 22 /srv/ root@target_ip:/srv/
# ssh root@target_ip -p 22
# ntpdate 192.168.2.33
# hwclock -w

function sync_and_check()
{
    client=$1
    salt $client state.highstate
    if [ $(salt $client dia.get_local_info | wc -l) -lt 2 ]; then
        salt $client saltutil.sync_modules
    fi
    result=$(salt $client dia.get_local_info | wc -l)
    return $result
}

if [ ! -f /root/bootstrap.sh ]; then
    curl -L -k http://bootstrap.saltstack.org > /root/bootstrap.sh
fi

if [ $? -ne 0 ]; then
    echo "Failed to fetch saltstack bootstrap script!"
    exit 1
fi

chmod +x /root/bootstrap.sh
/root/bootstrap.sh -M -N

if [ $? -ne 0 ]; then
    echo "Failed to execute bootstrap.sh."
    exit 1
fi

sleep 3

if [ $(ps aux | grep salt-master | grep -v grep | wc -l) -eq 0 ]; then
    echo "Failed to run up saltstack master!"
    exit 1;
fi

salt-key -Ay
client_list=$(salt-key -l acc | awk 'NR > 1 {print $1}' )

for client in $client_list
do
    echo $client
    result_lines=1
    count=0
    while [ "$result_lines" -lt 2 ] && [ "$count" -lt 10 ]; do
        sync_and_check $client
        result_lines=$?
        echo $result_lines
        count=$(($count + 1))
    done

    if [ "$count" -eq 10 ]; then
        echo $client >> ./not_ready_client.txt
    else
        now=$(date +"%F %X")
        salt $client cmd.run "date $now"
        salt $client cmd.run "echo %date% %time%"

        salt $client agent.minion_restart
        salt $client cmd.run "c:\\salt\\var\\logon.bat"
    fi
done
