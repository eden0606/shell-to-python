#!/bin/sh

# this is main config file, source it to pull in values

# LOGGER

logger() {
	local function="logger"
	local dt=$(date)
	local f=$1
	local l=$2
	local h=$3
	local m=$4
	echo="${dt}|${1}|${h}|${m}" >> "${f}"
}

logger
