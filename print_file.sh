#!/bin/bash

print_file() {
	echo "${2}" >> "${1}"
	echo $1
}

print_file "${1}" "${2}"

