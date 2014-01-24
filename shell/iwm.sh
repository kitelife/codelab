#!/bin/sh

function start_all()
{

    ROOT=`pwd`

    # start nsq

    NSQ_DIR="$ROOT/nsq"
    NSQLOOKUPD_BIN="$ROOT/nsq/bin/nsqlookupd"
    NSQD_BIN="$ROOT/nsq/bin/nsqd"
    NSQADMIN_BIN="$ROOT/nsq/bin/nsqadmin"

    if [ ! -d "$NSQ_DIR" ]; then
        echo "Not Exist NSQ source code!"
        exit 1
    fi
    if [ ! -f "$NSQLOOKUPD_BIN" ] || [ ! -f "$NSQD_BIN" ] || [ ! -f "$NSQADMIN_BIN" ];then
        export GOPATH=$NSQ_DIR
        if type go >/dev/null 2>&1; then
            go install github.com/bitly/nsq/nsqd
            go install github.com/bitly/nsq/nsqadmin
            go install github.com/bitly/nsq/nsqlookupd
        else
            echo "I can find the *go* command"
        fi
        echo "Finish to compile nsq!"
    fi
    if [ -f "$NSQLOOKUPD_BIN" ] && [ -f "$NSQD_BIN" ] && [ -f "$NSQADMIN_BIN" ]; then
        NSQ_LOG_DIR="/var/log/nsq"
        if [ ! -d "$NSQ_LOG_DIR" ]; then
            mkdir -p $NSQ_LOG_DIR
        fi
        $NSQLOOKUPD_BIN > $NSQ_LOG_DIR/nsqlookupd.log 2>&1 &
        $NSQD_BIN --lookupd-tcp-address=127.0.0.1:4160 > $NSQ_LOG_DIR/nsqd.log 2>&1 &
        $NSQADMIN_BIN --nsqd-http-address=127.0.0.1:4151 --template-dir=$NSQ_DIR/src/github.com/bitly/nsq/nsqadmin/templates > $NSQ_LOG_DIR/nsqadmin.log 2>&1 &
    else
        echo "I can't run up *nsq*!"
        exit 1
    fi
    ####################################################################################################################

    # start nsq client

    CLIENT_DIR="$ROOT/client"
    CLIENT_BIN="$ROOT/client/bin/nsq_client"
    CHECK_NSQD=$( ps aux | grep -v grep | grep $NSQD_BIN | wc -l)
    if [ ! -d "$CLIENT_DIR" ]; then
        echo "Not Exist NSQ client source code!"
        exit 1
    fi
    if [ ! -f "$CLIENT_BIN" ]; then
        export GOPATH=$CLIENT_DIR
        go install nsq_client
        echo "Finish to compile nsq client"
    fi
    if [ -f "$CLIENT_BIN" ] && [ $CHECK_NSQD -gt 0 ]; then
        CLIENT_LOG_DIR="/var/log/nsq_client"
        if [ ! -d "$CLIENT_LOG_DIR" ]; then
            mkdir -p $CLIENT_LOG_DIR
        fi
        $CLIENT_BIN --db-path=$CLIENT_DIR/db --nsqd-tcp-address=127.0.0.1:4150 > $CLIENT_LOG_DIR/client.log 2>&1 &
    else
        echo "I can't run up nsq client!"
        exit 1
    fi

    ####################################################################################################################

    # start local server webapp

    LOCAL_SERVER_WEBAPP_DIR="$ROOT/webapp/local_server"
    LOCAL_SERVER_WEBAPP_BIN="$LOCAL_SERVER_WEBAPP_DIR/src/big_brother/big_brother"
    CHECK_CLIENT=$( ps aux | grep -v grep | grep $CLIENT_BIN | wc -l)
    if [ ! -d "$LOCAL_SERVER_WEBAPP_DIR" ]; then
        echo "Not Exist local server webapp source code!"
        exit 1
    fi
    if [ ! -f "$LOCAL_SERVER_WEBAPP_BIN" ]; then
        export GOPATH=$LOCAL_SERVER_WEBAPP_DIR
        go install big_brother
        mv $LOCAL_SERVER_WEBAPP_DIR/bin/big_brother $LOCAL_SERVER_WEBAPP_BIN
    fi
    if [ -f "$LOCAL_SERVER_WEBAPP_BIN" ] && [ $CHECK_NSQD -gt 0 ] && [ $CHECK_CLIENT -gt "0" ]; then
        LOCAL_SERVER_WEBAPP_LOG_DIR="/var/log/local_server"
        if [ ! -d "$LOCAL_SERVER_WEBAPP_LOG_DIR" ]; then
            mkdir -p $LOCAL_SERVER_WEBAPP_LOG_DIR
        fi
        pushd $LOCAL_SERVER_WEBAPP_DIR/src/big_brother
        ./big_brother > $LOCAL_SERVER_WEBAPP_LOG_DIR/webapp.log 2>&1 &
        popd
    else
        echo "I can't run up local server webapp!"
        exit 1
    fi
    ####################################################################################################################
    # check running
    if [ $(ps aux | grep -v grep | grep $NSQLOOKUPD_BIN | wc -l) -gt 0 ]; then
        echo "Successfully to run up nsqlookupd"
    else
        echo "Failed to run up nsqlookupd"
    fi
    if [ $(ps aux | grep -v grep | grep $NSQD_BIN | wc -l) -gt 0 ]; then
        echo "Successfully to run up nsqd"
    else
        echo "Failed to run up nsqd"
    fi
    if [ $(ps aux | grep -v grep | grep $NSQADMIN_BIN | wc -l) -gt 0 ]; then
        echo "Successfully to run up nsqadmin"
    else
        echo "Failed to run up nsqadmin"
    fi
    if [ $(ps aux | grep -v grep | grep $CLIENT_BIN | wc -l) -gt 0 ]; then
        echo "Successfully to run up nsq client"
    else
        echo "Failed to run up nsq client"
    fi
    if [ $(ps aux | grep -v grep | grep ./big_brother | wc -l) -gt 0 ]; then
        echo "Successfully to run up big_brother"
    else
        echo "Failed to run up big_brother"
    fi

    ####################################################################################################################
    # over !
}

function stop_all()
{
    ROOT=`pwd`
    declare -a PROCESS_LIST=("$ROOT/nsq/bin/nsqlookupd" "$ROOT/nsq/bin/nsqd" "$ROOT/nsq/bin/nsqadmin" "$ROOT/client/bin/nsq_client" "./big_brother")
    for p in ${PROCESS_LIST[@]};do
        pid=$(ps aux | grep -v grep | grep $p | awk '{print $2}')
        if [ "$pid" != "" ];then
            kill -1 $pid
            echo "Stopping $p"
        fi
        pid_again=$(ps aux | grep -v grep | grep $p | awk '{print $2}')
        if [ "$pid_again" != "" ];then
            kill -9 $pid_again
            echo "Stopping $p again"
        fi
    done
}

function usage()
{
    echo "Usage: $1 start|stop|restart"
}

function main()
{
    if [ $# = 1 ];then
        if [ "$1" = "start" ];then
            start_all
        elif [ "$1" = "stop" ];then
            stop_all
        elif [ "$1" = "restart" ];then
            stop_all
            start_all
        else
            usage $0
            exit 1
        fi
    fi
}

main $@