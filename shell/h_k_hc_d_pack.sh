#!/bin/sh

rm -f *.tar.gz
rm -rf deploy_pack

mkdir deploy_pack

tar -cvzf BIND.tar.gz ./BIND
tar -cvzf HAProxy.tar.gz ./HAProxy
tar -cvzf HAProxyConsole.tar.gz ./HAProxyConsole
tar -cvzf Keepalived.tar.gz ./Keepalived

mv *.tar.gz deploy_pack/
cp deploy.sh run.sh tcpdump deploy_pack/

tar -cvzf deploy_pack.tar.gz ./deploy_pack

echo "*** Successfully! END ***"
