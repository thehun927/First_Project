#!/usr/bin/python

import csv
import sys
import os
import time
import hashlib

#path = "/home/attila/GitHub"
#log =
md5 = hashlib.md5()
path = raw_input("Enter a directory: ")
workingdir = os.getcwd()
print "Current working directory %s" % workingdir

os.chdir( path )

workingdir = os.getcwd()

print "Directory changed successfully to %s" % workingdir

#time.sleep(2)

for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):
    for name in files:
        print(os.path.join(root, name))
#        print >> log.txt
    for name in dirs:
        print(os.path.join(root, name))
#        print >> log.txt

