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

#declare global vars
server = "https://haveibeenpwned.com/api/v2/breachedaccount/"
sslVerify = True
address = str(args.address)
filename = str(args.filename)
lstEmail = ["info@example.com","example@example.com", "test@test.com"]
breached_emails = []

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
    breach_info()

def checkAddress(email):
    rate = 1.5
    check=requests.get(server + email + "?includeUnverified=true",
                 verify=sslVerify)
    #Check for 404 - 404 meajns that the API returned no results
    if str(check.status_code) == "404":
        print("[✓] " + email + " has not been breached.")
        time.sleep(rate)
        return False
    #Check for 200 status - 200 means that the API found a breach
    elif str(check.status_code) == "200":
        print("[X] " + email + " has been breached!")
        breach_email.append(email)
        time.sleep(rate)
        return True
    #Check for HTTP code 429(rate limit)   
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
      
def breach_info():
    rate = 1.5
    check=requests.get(server + email + "?includeUnverified=true",
                 verify=sslVerify)
    #Check for 404 - 404 meajns that the API returned no results
    if str(check.status_code) == "404":
        print("failure for checking " + email)
        time.sleep(rate)
        return False
    #Check for 200 status - 200 means that the API found a breach
    elif str(check.status_code) == "200":
        print(check)
        time.sleep(rate)
        return True
    #Check for HTTP code 429(rate limit)   
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
