#!/usr/bin/python

import csv
import sys
import os
import time
import hashlib
import difflib
from progressbar \
    import Bar,  ETA, ProgressBar, ReverseBar

def md5Checksum(filePath):                      #Function to generate MD5 Hash
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()        #Function to generate MD5 Hash

def countdown():
    print "Starting in 3.."
    time.sleep(1)
    print "2.."
    time.sleep(1)
    print "1.."
    time.sleep(1)

def backwardsBar():
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()

md5 = hashlib.md5()
Vlog = "/Users/attila/Desktop/Vlog.txt"

print "Current working directory %s" % os.getcwd()      #Prints the current working directory for reference
path = raw_input("Enter a directory to scan: ")         #Custom directory scanning

os.chdir(path)                            #Change the cwd to the user specified path
workingdir = os.getcwd()                   #set workingdir to the cwd

print "Directory changed successfully to %s" % workingdir       #Prints the changed directory for reference

#countdown()     #Countdown function
#backwardsBar()

seq = []
for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):   #Scan directories and files in the path variable
    for name in files:                          #For every file name in files scanned
        seq.append(str(os.path.join(root, name)))          #Write the path and name of the file
        #seq.append(str('\n'))

md = []
for item in seq:
    md5Checksum(item)
    md.append(md5Checksum(item))
    #md.append('\n')

Vlist = [line.strip() for line in open(Vlog, 'r')]

for index, item in enumerate(Vlist):
    print index, item
