import os
import shutil
import sys
import socket
import psutil

def check_reboot():
    """Checks if the computer needs a reboot."""
    result = os.path.exists("/run/reboot-required") # Returns True if the computer has a pending reboot.
    if result == True:
        print("\tThe computer needs to reboot.")
    else:
        print("\tNo reboot needed.")

def check_disk_usage(disk, min_gb, min_percent):
    """Return True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

def check_network():
    """Checks if the computer is connected to the network/internet"""
    try:
        socket.gethostbyname("www.google.com")
        print("\tYou are connected to the network.")
    except:
        print("\tYou are not connected to the network.")

def check_cpu():
    """Checks if the cpu usage is grater than 75%"""
    if psutil.cpu_percent(1) > 75:
        print("\tCPU usage is grater than 75%!!")
    else:
        print("\tCPU usage is good.")

def main():
    print("Comprehensive system check:")
    check_network()
    check_reboot()
    check_cpu()
    #Check for at least 10 GB and 20% free
    if not check_disk_usage(disk="/", min_gb=10, min_percent=20):
        print("\tDisk Usage: ERROR: Not enough space.")
        sys.exit(1)
    else: 
        print("\tDisk Usage: Ok.")
        sys.exit(0)

main()