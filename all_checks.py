#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    result = os.path.exists("/run/reboot-required")
    if result == True:
        print("\tThe computer needs to reboot.")
    else:
        print("\tNo reboot needed.")

def check_disk_usage(disk, min_absolute, min_percent):
    """Return True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

def main():
    print("Comprehensive system check:")
    #calling the check_reboot function
    check_reboot()
    #Check for at least 10 GB and 20% free
    if not check_disk_usage("/", 10, 20):
        print("\tDisk Usage: ERROR: Not enough space.")
        sys.exit(1)
    else: 
        print("\tDisk Usage: Everything is ok.")
        sys.exit(0)

main()
