#! /usr/local/bin/python3.7

import time

def follow(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0,1)
			continue
		yield line


follow('/Users/davidlee/dsfsd.py')