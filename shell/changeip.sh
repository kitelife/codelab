#!/bin/bash

# There is a script named lab_interfaces for lab network configuration
# and a script named dor_interfaces for dormitory network configuration

if [ "$1" = "lab" ];then
	cp lab_interfaces interfaces
else
	if [ "$1" = "dor" ];then
		cp dor_interfaces interfaces
	fi
fi

if [ -f "interfaces" ];then
	sudo cp interfaces /etc/network/
	sudo /etc/init.d/networking restart
	rm interfaces
	python ~/Software/goagent/local/proxy.py
fi
