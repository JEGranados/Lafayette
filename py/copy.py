import time, serial, csv, os, json
from datetime import datetime

# Declare variables
usb="/media/alecasti/ESD-USB"

# Get current directory
dir = os.path.dirname(os.path.realpath(__file__))

def checkUSB():
    if os.path.exists(usb):
        print("USB connected")
        return True
    else:
        print("USB not connected")
        return False

# Main loop
while True:
    if checkUSB():
        print("Copying files...")
        os.system("cp " + dir + "/*.csv " + usb)
        os.system("cp " + dir + "/*.json " + usb)
        print("Files copied")
        os.system("rm " + dir + "/*.csv")
        os.system("rm " + dir + "/*.json")
        break
    else:
        time.sleep(5)
 
