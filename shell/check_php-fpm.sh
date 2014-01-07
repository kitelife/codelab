#!/bin/sh
rhfl=$( curl -I -s http://sh.ecc.com/login_entrance.php | head -1 | tr " " "\n" | head -2 | tail -1 )
if [ "$rhfl" == "502" ]; then
    echo "`date` sh.ecc.com fall into 502 ..., Now i try to restart php-fpm"
    /root/script/php-fpm stop
    /root/script/php-fpm start
    if [ $( ps -e | grep php-fpm | wc -l ) -gt 0 ]; then
        echo "`date` succeed to restart php-fpm"
    else
        echo "`date` failed to restart php-fpm"
    fi
else
    echo "`date`,  $rhfl"
fi
