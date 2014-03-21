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
log = "C:/Users/Owner/Documents/GitHub/PY-Virus-Scanner/log.txt"
md5 = hashlib.md5()
path = raw_input("Enter a directory: ")
workingdir = os.getcwd()
print "Current working directory %s" % workingdir

os.chdir(path)

workingdir = os.getcwd()

print "Directory changed successfully to %s" % workingdir

#time.sleep(2)

with open(log, 'w') as F:
    for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):
        for name in files:
#            print(os.path.join(root, name))
            F.write(str(os.path.join(root, name)))
            F.write(str('\n'))
        for name in dirs:
#            print(os.path.join(root, name))
            F.write(str(os.path.join(root, name)))
            F.write(str('\n'))

with open(log) as F:
    for line in F:
        while True:
            data = F.read()
            if not data:
                break
            md5.update(data)
        print(md5.hexdigest())

