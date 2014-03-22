#!/usr/bin/python

import csv
import sys
import os
import time
import hashlib
import difflib

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

md5 = hashlib.md5()
log = "/Users/attila/Desktop/log.txt"
Mlog = "/Users/attila/Desktop/Mlog.txt"
Vlog = "/Users/attila/Desktop/Vlog.txt"
Output = "/Users/attila/Desktop/Output.txt"

print "Current working directory %s" % os.getcwd()      #Prints the current working directory for reference
path = raw_input("Enter a directory to scan: ")         #Custom directory scanning

os.chdir(path)                            #Change the cwd to the user specified path
workingdir = os.getcwd()                   #set workingdir to the cwd

print "Directory changed successfully to %s" % workingdir       #Prints the changed directory for reference

countdown()     #Countdown function

with open(log, 'w') as F:       #Open log file
    for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):   #Scan directories and files in the path variable
        for name in files:                          #For every file name in files scanned
#            print(os.path.join(root, name))
            F.write(str(os.path.join(root, name)))          #Write the path and name of the file
            F.write(str('\n'))                              #New line

with open(Mlog, 'w') as FM:                 #Open MD5 Log File
    FM.write("MD5 HASHES SCANNED FROM DIRECTORY \n\n")      #Add title
    F = open(log).read().splitlines()                       #Open the first log and read each line
    for line in F:                      #For every line in the first log
        md5Checksum(line)                       #Generate an MD5 checksum
        FM.write(line.rstrip('\n') + "\n" + md5Checksum(line) + "\n")           #Copy the direcotry and file name and put the hash under it
        FM.write(str('\n'))                     #New line

with open(Mlog, 'r') as M:              #Open MD5 Log file
    with open(Vlog, 'r') as V:          #Open Log file with virus hashes
        same = set(M).intersection(V)               #
same.discard("\n")
with open(Output, 'w') as FO:
    for line in same:
        FO.write(line)
