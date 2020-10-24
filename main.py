from configparser import ConfigParser
import os

clear = lambda: os.system('clear')

#CREATE CONFIG
config_object = ConfigParser()

config_object["CONFIG"] = {
    "trashAfter": "",     #in seconds
}

with open('config.ini', 'w') as conf:
    config_object.write(conf)


# CONFIG
sel = "100"
while int(sel) > 5 or int(sel) < 0:
    clear()
    print("\n >_  downbloats configuration")
    sel = input("\n[STEP 1] The clean-up process trashes all files, that have not been accessed for:\n [1] One hour\n [2] Three hours\n [3] One day\n [4] Three days\n [5] One week\n\n Your choice? (1/2/3/4/5) ")

clear()
print("\n >_  downbloats configuration")

config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["CONFIG"]

if int(sel) == 1:
    print("\n[STEP 1]  The clean-up process will trash all files, that have not been accessed for one hour.\n")
    userinfo["trashAfter"] = "3600"
elif int(sel) == 2:
    print("\n[STEP 1]  The clean-up process will trash all files, that have not been accessed for three hours.\n")
    userinfo["trashAfter"] = "10800"
elif int(sel) == 3:
    print("\n[STEP 1]  The clean-up process will trash all files, that have not been accessed for one day.\n")
    userinfo["trashAfter"] = "86400"
elif int(sel) == 4:
    print("\n[STEP 1]  The clean-up process will trash all files, that have not been accessed for three days.\n")
    userinfo["trashAfter"] = "259200"
elif int(sel) == 5:
    print("\n[STEP 1]  The clean-up process will trash all files, that have not been accessed for one week.\n")
    userinfo["trashAfter"] = "604800"

with open('config.ini', 'w') as conf:
    config_object.write(conf)


# CLEANUP sel
sel = ""
while sel.lower() != "y" and sel.lower() != "n":
    sel = input("[?]  Do you want to run the ~/Downlaods/ clean-up? (Y/n)")

if sel.lower() == "y":
    clear()
    os.system('python3 clean.py')

