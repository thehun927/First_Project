#!/usr/bin/python

import os
import sys

path = "C:/Users/Owner/Desktop"
workingdir = os.getcwd()
print "Current working directory %s" % workingdir

os.chdir( path )

workingdir = os.getcwd()

print "Directory changed successfully to %s" % workingdir

for root, dirs, files in os.walk(".", followlinks=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))






