#!/usr/bin/python

import sys
# enumscript.py
# usage: enumscript.py file [> enum.txt]
# reads ip list and calls enum4linux for each ip
# Next version: write all output to one file
#***************************************
f = open(sys.argv[1],"r")
for line in f:
	# call enum4linux
f.close()
