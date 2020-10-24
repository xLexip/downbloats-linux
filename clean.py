import os, glob, time, getpass, pathlib, subprocess
from configparser import ConfigParser
from send2trash import send2trash
from datetime import datetime
from stat import *

clear = lambda: os.system('clear')
print("\033[1m\033[96m>_  downbloats cleaning\033[0m")


# READ CONFIG
if os.path.isfile(str(pathlib.Path(__file__).parent.absolute())+"/config.ini"):
    config_object = ConfigParser()
    config_object.read(str(pathlib.Path(__file__).parent.absolute())+"/config.ini")
else:
    print("\n\033[91m[!] Config file not found, running main.py...\033[0m")
    input("\nPress Enter to continue...")
    clear()
    os.system('python3 '+str(pathlib.Path(__file__).parent.absolute())+'/main.py')
    exit()

info = config_object["CONFIG"]
trashAccessedAfter = info["trashAfter"]


# GET DOWNLAODS PATH
path = "/home/"+getpass.getuser()+"/Downloads/*"


# SCAN PATH
files = []
for file in glob.glob(path):
    files.append(file)
print("\n\033[94m[i]\033[0m  Scanning "+str(len(files))+" Files in Downloads...")


# CLEAN PATH
cleanedSth = False
for file in files:
    try:
        st = os.stat(file)
    except IOError:
        print("\033[91m[!]\033[0m  Cannot get information about :", file.rsplit('/', 1)[-1])
    else:
        if (int(time.mktime(time.localtime())) - int(st[ST_ATIME])) >= float(trashAccessedAfter):
            send2trash(file)
            print("\033[91m[>]\033[0m  Trashed: "+file.rsplit('/', 1)[-1])
            cleanedSth = True

if not cleanedSth:
    print("\033[92m\n[✓]\033[0m  Nothing to clean.\n")
else:
    print("\033[92m\n[✓]\033[0m  Cleaning completed.\n")