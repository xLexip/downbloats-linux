import os

clear = lambda: os.system('clear')

clear()
print("\n >_  downbloats setup")

# CLEANUP SELECTION
selection = ""
while selection.lower() != "y" and selection.lower() != "n":
    selection = input("[?]  Do you want to run the ~/Downlaods/ clean-up? (Y/n)")

if selection.lower() == "y":
    clear()
    os.system('python3 clean.py')
    clear()

