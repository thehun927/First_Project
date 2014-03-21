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
md5 = hashlib.md5()
workingdir = os.getcwd()
log = "/home/attila/Desktop"
path = raw_input("Enter a directory to scan: ")
print "Current working directory %s" % workingdir

os.chdir(path)

print "Directory changed successfully to %s" % workingdir

print "Starting in 3.."
time.sleep(1)
print "2.."
time.sleep(1)
print "1.."
time.sleep(1)

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

F = open(log).read().splitlines()
for line in F:
    md5Checksum(line)
    print("The MD5 Checksum of the file is ", md5Checksum(line))
