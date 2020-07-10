#!/bin/sh

function Hello() {
	local NAME=$1
	echo "hello $NAME welcome to my world"
	echo ["hi", "bye", "goodbye"] >> output
	tr -s ' '  '\n' < output > hello
	
}

#echo "calling hello function"
Hello Eden







