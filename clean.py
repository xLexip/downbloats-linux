import os, glob, time, getpass
from configparser import ConfigParser
from send2trash import send2trash
from datetime import datetime
from stat import *

clear = lambda: os.system('clear')
clear();

print("\n >_  downbloats cleaning")

# CONFIG
#Read config.ini file
if os.path.isfile("config.ini"):
    config_object = ConfigParser()
    config_object.read("config.ini")
else:
    print("\n[!] Config file not found, running main.py...")
    input("\nPress Enter to continue...")
    clear()
    os.system('python3 main.py')
    exit()

#Get file timeout
userinfo = config_object["CONFIG"]
trashAccessedAfter = userinfo["trashAfter"]

# GET PATH
username = getpass.getuser()
path = "/home/"+username+"/Downloads/*"

# SCAN PATH
files = []
for file in glob.glob(path):
    files.append(file)
print("\n[i]  Found "+str(len(files))+" Files in Downloads...")

# CLEAN PATH
cleanedSth = 0
for file in files:
    try:
        st = os.stat(file)
    except IOError:
        print("[!]  Cannot get information about :", file.rsplit('/', 1)[-1])
    else:
        if float(time.mktime(time.localtime()) - st[ST_ATIME]) >= float(trashAccessedAfter):
            send2trash(file)
            print("[i]  Trashed: "+file.rsplit('/', 1)[-1])
            cleanedSth = 1

if cleanedSth == 0:
    print("[i] Nothing to clean.")

input("\nPress Enter to continue...")


        
