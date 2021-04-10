import os, glob, time, shutil, getpass, pathlib, subprocess
from configparser import ConfigParser
from send2trash import send2trash
from datetime import datetime
from stat import *

def checkDirectory(pPath):  #CHECK PATH RECURSIVE
    files2 = []
    for file in glob.glob(pPath+"/*"):
        files2.append(file)

    cleanedSth = False
    for file in files2:
        try:
            st = os.stat(file)
        except IOError:
            print("\033[91m[!]\033[0m  Cannot get information about :", file.rsplit('/', 1)[-1])
        else:
            if(os.path.isdir(file)):
                    return checkDirectory(file)
            elif (int(time.mktime(time.localtime())) - int(st[ST_ATIME])) < float(trashAccessedAfter):
                return False
    return True


cleanedSth = False
clear = lambda: os.system('clear')
clear()

# Remove the above line to avoid multiple printing
print("\033[F\033[F\033[F\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K");

print("\033[F\033[1m\033[96m>_  downbloats cleaning\033[0m")


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


# SCAN PATH
files = []
for file in glob.glob("/home/"+getpass.getuser()+"/Downloads/*"):
    files.append(file)
print("\n\033[94m[i]\033[0m  Scanning "+str(len(files))+" Items in Downlaods...")


# CLEAN PATH
cleanedSth = False
for file in files:
    try:
        st = os.stat(file)
    except IOError:
        print("\033[91m[!]\033[0m  Cannot get information about :", file.rsplit('/', 1)[-1])
    else:
        if(os.path.isdir(file)):
                if checkDirectory(file):
                    send2trash(file)
                    print("\033[91m[>]\033[0m  Trashed Dir.:    "+file.rsplit('/', 1)[-1])

        elif (int(time.mktime(time.localtime())) - int(st[ST_ATIME])) >= float(trashAccessedAfter):
            send2trash(file)
            print("\033[91m[>]\033[0m  Trashed File:    "+file.rsplit('/', 1)[-1])
            cleanedSth = True

if not cleanedSth:
    print("\033[92m\n[✓]\033[0m  Nothing to clean.\n")
else:
    print("\033[92m\n[✓]\033[0m  Cleaning completed.\n")