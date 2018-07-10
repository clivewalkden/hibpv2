#!/usr/bin/python hibp
# -*- coding: utf-8 -*-

# Modified version of Jeffrey Mustard's - removing any customization and colours
# The version you're using was modified by Jeffrey Mustard | Contact:  (https://github.com/JeffreyMustard)
# Original Author = Laurens Houben | Contact: (https://github.com/houbbit)

import requests
import time 
import argparse

parser = argparse.ArgumentParser(description="Verify if email address has been pwned")
parser.add_argument("-a", dest="address",
                  help="Single email address to be checked")
parser.add_argument("-f", dest="filename",
                  help="File to be checked with one email addresses per line")
args = parser.parse_args()

rate = 1.5
server = "https://haveibeenpwned.com/api/v2/breachedaccount/"
sslVerify = True

def main():
    if address != "None":
        checkAddress(address)
    elif filename != "None":
        email = [line.rstrip('\n') for line in open(filename)]
        for email in email:
            checkAddress(email)
    else:
        for email in lstEmail:
            checkAddress(email)

def checkAddress(email):
    check=requests.get(server + email + "?includeUnverified=true",
                 verify=sslVerify)
    if str(check.status_code) == "404":
        print("[✓] " + email + " has not been breached.")
        time.sleep(rate)
        return False
    elif str(check.status_code) == "200":
        print("[X] " + email + " has been breached!")
        time.sleep(rate)
        return True
    elif str(check.status_code) == "429":
        print("[!] Rate limit exceeded, server instructed us to retry after " + check.headers['Retry-After'] + " seconds")
        print("    Refer to acceptable use of API: https://haveibeenpwned.com/API/v2#AcceptableUse")
        rate = float(check.headers['Retry-After'])
        time.sleep(rate)
        checkAddress(email)
    else:
        print("[!] Something went wrong while checking " + email)
        time.sleep(rate)
        return True

if __name__ == "__main__":
    main()
