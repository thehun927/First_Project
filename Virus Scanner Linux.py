#!/usr/bin/python

import csv
import sys
import os
import time
import hashlib

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

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

with open('C:/Users/Owner/Desktop/log.txt', 'w') as F:
    for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):
        for name in files:
            print(os.path.join(root, name))
#           print >> log.txt
        for name in dirs:
            print(os.path.join(root, name))
#           print >> log.txt

