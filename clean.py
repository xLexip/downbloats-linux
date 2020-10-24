import os, glob, time, getpass
from send2trash import send2trash
from datetime import datetime
from stat import *
###

print("\n >_  downbloats cleaning")

# CONFIG
trashAccessedAfter = 172800 #TwoDays

# GET PATH
username = getpass.getuser()
path = "/home/"+username+"/Downloads/*"

# SCAN PATH
files = []
for file in glob.glob(path):
    files.append(file)
print("[i]  Found "+str(len(files))+" Files in Downloads...")

# CLEAN PATH
cleanedSth = 0
for file in files:
    try:
        st = os.stat(file)
    except IOError:
        print("[!]  Cannot get information about :", file.rsplit('/', 1)[-1])
    else:
        if (time.mktime(time.localtime()) - st[ST_ATIME]) >= trashAccessedAfter:
            send2trash(file)
            print("[i]  Trashed: "+file.rsplit('/', 1)[-1])
            cleanedSth = 1

if cleanedSth == 0:
    print("[i] Nothing to clean.")

input("\nPress Enter to continue...")


        
