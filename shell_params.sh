#!/bin/sh

s2p() {
	local VAR1=$(date)
	local VAR2=$1
#	local VAR3=$2
	echo $VAR1
	python python_params.py $VAR1 $VAR2 
}

echo "Working..."
s2p ${1} ${2}
