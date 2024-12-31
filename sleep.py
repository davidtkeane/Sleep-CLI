#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Title: Send your Macbook's to Sleep over the Network using CLI
#
# Created by Ranger (Dec 2024) Version 1.0.0
# Modified by David Keane (Dec 31st 2024) Version 2.0.1
#
# Description:
# This script is designed to work on Mac systems only.
# The script sends both the local and remote macs to sleep.
#
# Functionality:
# The remote mac is specified by the user and host.
# The script uses the pmset command to send the macs to sleep.
# The script also uses the ssh command to send the remote mac to sleep.
# The script uses the subprocess module to run shell commands.
# The script uses the platform module to get the system type.
# The script uses the ipaddress module to validate the remote host.
# The script uses the time module to add a delay for the remote mac to sleep.
# The script uses the os module to check the system type.
# The script uses the print function to display messages.
# The script uses the if __name__ == "__main__": to run the script.

# Import the necessary modules.
import subprocess
import platform
import os
import time
import ipaddress

def _run_command(command, check_error=True):
    """Helper function to execute shell commands and return output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=check_error)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if check_error:
           print(f"Error executing command {command}: {e}")
        return None


def send_mac_to_sleep(target, user=None, host=None):
    """Sends a specified mac to sleep.
       Keyword arguments:
       target - The target mac, "local" or "remote"
       user - the username of remote host
       host - the remote hostname or ip
    """
    if target == "local":
        command = ['pmset', 'sleepnow'] #this will send the local mac to sleep
        output = _run_command(command, check_error=False) #do not check for errors.
        if output is None:
            print("Local mac has gone to sleep")
        else:
            print("Local mac has gone to sleep") # print the message even if output is detected.

    elif target == "remote":
        if not user or not host:
            print ("Please provide user and host for remote mac")
            return None
        else:
            #Test the connection.
            test_connection = ['ssh', f'{user}@{host}', 'echo', '"Connection successful"']
            test_output = _run_command(test_connection, check_error = False)
            if "Connection successful" not in test_output:
                print(f"Error connecting to {host}. Ensure that the remote machine is on and SSH is enabled.")
                return None
            command = ['ssh', f'{user}@{host}', 'pmset', 'sleepnow']
            output = _run_command(command, check_error=False) #Do not check for errors with the sleep command.
            if output is None:
                print(f"Remote mac {host} has gone to sleep")
            else:
               print(f"Error, remote mac {host} may have not gone to sleep.\n Output: {output}")

    else:
       print ("Invalid target, please choose 'local' or 'remote'")
       return None

def sleep_all_macs():
    """Sends both macs to sleep"""
    print ("Going to sleep")


    secondary_user = "rangersmyth"  # Replace with your secondary username
    secondary_host = "192.168.1.7" # Replace with your secondary host/IP

    primary_mac = platform.system() #Gets the system type.

    if primary_mac != "Darwin":
        print ("This script is designed to only work on Darwin based systems (Mac)")
        return None
    if secondary_host and secondary_user:
        try:
            ipaddress.ip_address(secondary_host) # check if the ip is a valid ip.
            #Test connection.
            if send_mac_to_sleep(target="remote", user=secondary_user, host=secondary_host) is None: #Test for connection errors.
               print (f"Failed to connect to {secondary_host}")
            else:
                time.sleep(2)  #Add a small delay for remote mac to sleep.
        except ValueError:
             print ("Invalid remote host, skipping...")

    send_mac_to_sleep(target="local") # Send the local mac to sleep.

if __name__ == "__main__":
     sleep_all_macs()