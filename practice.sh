#!/bin/sh

pipes() {
	local NAME1=$1
	local NAME2=$2
	local NAME3=$3
	local NAME4=$4
	echo "${NAME1}|${NAME2}|${NAME3}" >> "${NAME4}"
}

echo "Names added to file!"
pipes ${1} ${2} ${3} ${4}

# pipes takes in parameters and redirects echo string "NAME1|NAME2|NAME3" into text file named 
# the parameter NAME4 if NAME4 does not exist, a new one is created
# if one already exists, names are appended to the end of the document
