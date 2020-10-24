import os, sys, time, getpass, pathlib, subprocess
from configparser import ConfigParser

clear = lambda: os.system('clear')

# CHECK FOR SUDO RIGHTS
if os.geteuid() == 0:
    print("[✗]  Do not run this with sudo privileges! Running without sudo...")
    sys.exit()
else:
    clear()
    print("\n >_  downbloats configuration\n")

#CREATE CONFIG
config_object = ConfigParser()

config_object["CONFIG"] = {
    "trashAfter": "",     #in seconds
}

with open('config.ini', 'w') as conf:
    config_object.write(conf)


# CONFIG PROMPT
sel = "100"
while int(sel) > 5 or int(sel) < 1:
    sel = input("\n[?] The clean-up process should trash all files, that have not been accessed for at least:\n [1] One hour\n [2] Three hours\n [3] One day\n [4] Three days\n [5] One week\n\n Your choice? (1/2/3/4/5) ")
    try: 
        int(sel)
    except ValueError as e:
        sel = "100"

clear()
print("\n >_  downbloats configuration")

config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["CONFIG"]
choice1 = ""

if int(sel) == 1:
    choice1 = "\n[✓]  The clean-up process will trash all files, that have not been accessed for one hour.\n"
    userinfo["trashAfter"] = "3600"
elif int(sel) == 2:
    choice1 = "\n[✓]  The clean-up process will trash all files, that have not been accessed for three hours.\n"
    userinfo["trashAfter"] = "10800"
elif int(sel) == 3:
    choice1 = "\n[✓]  The clean-up process will trash all files, that have not been accessed for one day.\n"
    userinfo["trashAfter"] = "86400"
elif int(sel) == 4:
    choice1 = "\n[✓]  The clean-up process will trash all files, that have not been accessed for three days.\n"
    userinfo["trashAfter"] = "259200"
elif int(sel) == 5:
    choice1 = "\n[✓]  The clean-up process will trash all files, that have not been accessed for one week."
    userinfo["trashAfter"] = "604800"

print(choice1)

with open('config.ini', 'w') as conf:
    config_object.write(conf)


# SCHEDULING PROMPT
sel = 100;
while int(sel) > 3 or int(sel) < 1:
    sel = input("[?] Select how you want to schedule the clean-up:\n[1] Not at all\n[2] On system start-up\n[3] On system start-up and every hour\n\nYour choice? (1/2/3)")
    try: 
        int(sel)
    except ValueError as e:
        sel = "100"

clear()
print("\n >_  your downbloats configuration")
print(choice1)

if sel.lower() == "1":
    os.system('crontab -u '+getpass.getuser()+' -l | grep -v "@reboot python3 '+str(pathlib.Path().absolute())+'/clean.py &" | crontab -u '+getpass.getuser()+' -')
    os.system('crontab -u '+getpass.getuser()+' -l | grep -v "python3 '+str(pathlib.Path().absolute())+'/clean.py" | crontab -u '+getpass.getuser()+' -')
    print("[✓]  The clean-up won't be run automatically.\n")

elif sel.lower() == "2":
    os.system('crontab -u '+getpass.getuser()+' -l | grep -v "python3 '+str(pathlib.Path().absolute())+'/clean.py" | crontab -u '+getpass.getuser()+' -')
    os.system('(crontab -l ; echo "@reboot python3 '+str(pathlib.Path().absolute())+'/clean.py &") | sort - | uniq - | crontab -')
    print("[✓]  The clean-up will be run on start-up.\n")

elif sel.lower() == "3":
    os.system('(crontab -l ; echo "@reboot python3 '+str(pathlib.Path().absolute())+'/clean.py &") | sort - | uniq - | crontab -')
    os.system('(crontab -l ; echo "30 * * * * python3 '+str(pathlib.Path().absolute())+'/clean.py") | sort - | uniq - | crontab -')
    print("[✓]  The clean-up will be run on start-up and every hour at half past.\n")

input("\nPress Enter to continue...")


# RUN CLEANUP
os.system('python3 clean.py')