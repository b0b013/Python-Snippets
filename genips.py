#!/usr/bin/python

import sys
# genips.py
# usage: genips.py network ip_start ip_end filename
# reads generates ip list
# really basic. think class C network for now.
#***************************************
network =  sys.argv[1]
ip_start = int(sys.argv[2])
ip_end = int(sys.argv[3]) + 1
f =  open(sys.argv[4],"w")
for x in range(ip_start, ip_end):
	f.write(network + '.' + str(x) + '\n')
f.close()
