#!/bin/sh

s2p() {
	local VAR1=$1
#	local VAR2=$2
#	local VAR3=$3
	python python_params.py $VAR1
}

echo "Working..."
s2p ${1}
