#!/usr/bin/python

import sys
# readfile.py
# usage: readfile.py filename
# reads file line by line and prints it
#***************************************

f = open(sys.argv[1],"r")
for line in f:
	print line,
f.close()
