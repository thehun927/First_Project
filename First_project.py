import os
import sys

workingdir = os.getcwd()
recursive = False;
movies = []

if (len(sys.argv) > 1):
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-r'):
            recursive = True;
        if (sys.argv[i].startswith("-d=")):
            workingdir = sys.argv[i].replace("-d=", "")

#print(workingdir)

if recursive:
    for dirname, dirnames, filenames in os.walk(workingdir):
        for subdirname in dirnames:
            dir = os.path.join(dirname.replace(workingdir, ""), subdirname)
            movies.append(dir)
        for filename in filenames:
            cleanfile = os.path.join(dirname.replace(workingdir, ""), filename)
            file = os.path.join(dirname, filename)
            movies.append(cleanfile + " " + str(os.path.getsize(file)) + "B")
else:
    movies = os.listdir(workingdir)
    for i in range(len(movies)):
        file = os.path.join(workingdir, movies[i])
        movies[i] = movies[i] + " " + str(os.path.getsize(file)) + "B"

for i in range(len(movies)):
    #print(movies[i])
