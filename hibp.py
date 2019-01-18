#!/usr/bin/python hibp
# -*- coding: utf-8 -*-

# Modified version of Jeffrey Mustard's - removing any customization and colours
# The version you're using was modified by Jeffrey Mustard | Contact:  (https://github.com/JeffreyMustard)
# Original Author = Laurens Houben | Contact: (https://github.com/houbbit)

import requests
import time
import argparse
import json
import os
import logging

parser = argparse.ArgumentParser(description="Verify if email address has been pwned")
parser.add_argument("-a", dest="address",
                    help="Single email address to be checked")
parser.add_argument("-f", dest="filename",
                    help="File to be checked with one email addresses per line")
parser.add_argument("-o", dest="output",
                    help="File to written to")
args = parser.parse_args()

# declare global vars
server = "https://haveibeenpwned.com/api/breachedaccount/"
sslVerify = True
address = str(args.address)
filename = str(args.filename)
output = str(args.output)
lstEmail = ["info@example.com","example@example.com", "test@test.com"]
breached_emails = []
rate = 1.6
headers = {
    'user-agent': 'Python HIBP/0.0.1',
    'api-version': '2'
}
data = {}


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
    global rate
    global headers
    global data
    logger = init_logging()
    check = requests.get(server + email + "?includeUnverified=true", verify=sslVerify, headers=headers)
    # Check for 404 - 404 means that the API returned no results
    if str(check.status_code) == "404":
        print("[✓] " + email + " has not been breached.")
        time.sleep(rate)
        return False
    # Check for 200 status - 200 means that the API found a breach
    elif str(check.status_code) == "200":
        print("[X] " + email + " has been breached!")
        jsondata = json.loads(check.text)
        data[email] = {}
        breaches = {}
        for x in range(0, len(jsondata)):
            breaches[jsondata[x]['Name']] = {'url': jsondata[x]['Domain'], 'breachdate': jsondata[x]['BreachDate']}

        data[email] = breaches
        breached_emails.append(email)
        time.sleep(rate)
        return True
    # Check for HTTP code 429(rate limit)
    elif str(check.status_code) == "429":
        print(
            "[!] Rate limit exceeded, server instructed us to retry after " + check.headers['Retry-After'] + " seconds")
        print("    Refer to acceptable use of API: https://haveibeenpwned.com/API/v2#AcceptableUse")
        rate = float(check.headers['Retry-After'])
        time.sleep(rate)
        checkAddress(email)
    else:
        print("[!] Something went wrong while checking " + email)
        print(check.content)
        time.sleep(rate)
        return True


def breach_info():
    global rate
    global headers
    global data

    if len(data):
        for email, resultdata in data.items():
            print("Breach info for: " + email)
            for name, breachdata in resultdata.items():
                print("!------ " + name + " ------!")
                print("Information: ")
                for k, v in breachdata.items():
                    print('\t' + k + ': ' + v)
    else:
        print("[!] Well done there are no breaches in the adddresses supplied")
        return True


def init_logging():
    rootlogger = logging.getLogger('my_logger')

    LOG_DIR = os.getcwd() + '/' + 'logs'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    filehandler = logging.FileHandler("{0}/{1}.log".format(LOG_DIR, "g2"))
    rootlogger.addHandler(filehandler)

    rootlogger.setLevel(logging.DEBUG)

    consolehandler = logging.StreamHandler()
    rootlogger.addHandler(consolehandler)

    return rootlogger


if __name__ == "__main__":
    main()
