# Comprehensiver System Check
This Python script performs a comprehensive system check to ensure yor computer is
running smoothly. It checks for various factors such as pending reboots, disk space,
network connectivity, and CPU usage.

## Features
    Reboot Checks: Detects if the computer needs a reboot.
    Disk Space Check: Verifies that there is enough free disk space.
    Network Check: Determines if the computer is connected to the network/internet.
    CPU Usage Check: Monitors CPU usage to identify high usage levels.

## Requirements
    Python
    The following modules:
        shutil, os, sys, socket, and psutil

## Usage
Customize the script (if needed) by adjusting the parameters in the 'main()' function:
    Modify the min_gb and min_percent values in check_disk_usage() to set your desired
        disk space thresholds.
    Customize the error message or thresholds in the other functions as necessary.
The script will perform the system checks and display the results. If any issues are detected, it will provide error messages and return a non-zero exit code. A successful check will return a zero exit code.