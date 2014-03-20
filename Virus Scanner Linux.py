#!/usr/bin/python

import csv
import sys
import os
import hashlib

#path = "/home/attila/GitHub"
path = raw_input("Enter a directory: ")
workingdir = os.getcwd()
print "Current working directory %s" % workingdir

os.chdir( path )

workingdir = os.getcwd()

print "Directory changed successfully to %s" % workingdir

for root, dirs, files in os.walk(onerror=None, topdown=True, followlinks=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

