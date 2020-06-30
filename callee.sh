#!/bin/bash

#add() {
#	return $(($1+$2))
#}

#add ${1} ${2}


log() {
	echo "${2}" >> "${1}"
	echo $1
}

log ${1} ${2}


