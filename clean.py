import os, glob, time, getpass
from send2trash import send2trash
from datetime import datetime
from stat import *


# CONFIG
trashAccessedAfter = 172800 #TwoDays

# GET PATH
username = getpass.getuser()
path = "/home/"+username+"/Downloads/*"

# SCAN PATH
files = []
for file in glob.glob(path):
    files.append(file)
print("Found "+str(len(files))+" Files in Downloads...")

# CLEAN PATH
for file in files:
    try:
        st = os.stat(file)
    except IOError:
        print("ERR:  Cannot get information about :", file.rsplit('/', 1)[-1])
    else:
        if (time.mktime(time.localtime()) - st[ST_ATIME]) >= trashAccessedAfter:
            send2trash(file)
            print("Trashed: "+file.rsplit('/', 1)[-1])


        
