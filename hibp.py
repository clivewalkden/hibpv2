#!/usr/bin/python hibp
# -*- coding: utf-8 -*-

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
server = "haveibeenpwned.com"
sslVerify = True

OKGREEN=('\033[92m')
WARNING=('\033[93m')
FAILRED=('\033[91m')
ENDC=('\033[0m')
blu3=('\033[94m')
p1nk=('\033[95m')
l1n3=(p1nk + "<==========================================================================================================================================================================================================================>")

address = str(args.address)
filename = str(args.filename)
lstEmail = ["info@example.com","example@example.com", "test@test.com"]
print('\n')
print('\n')
print('\n')
print(l1n3)
print('\n')
print('\n')
print(blu3 + "                   `-:/+oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyoo+/:-`                                                                                                                      ")
print(blu3 + "              `:+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+:.                                                                                                                   ")
print(blu3 + "           `/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo/.                                                                                                                ")
print(blu3 + "         -oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo:                                                                                                              ")
print(blu3 + "       .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-                                                                                                            ")
print(blu3 + "     `+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+.           `.......`                     /ydmmdo      /ydmmdo                                             ")
print(blu3 + "    .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-          +yyyydMM-                   `dN+.  ``    `dMo.  ``                                             ")
print(blu3 + "   .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:              :Md      ./ooo/`       yMo          oMo       .+- .+oo/`     `/ooo/.   `+/     `+/        ")
print(blu3 + "  `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-             yM/    :dmo//+mN:  +yyyNMyyyyo` /yyyNMyyyyy`  +Myyd+/oMm   -yNy//+dM+   mM-    /My        ")
print(blu3 + "  oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`           .MN`   +My`  `-dM:  :::yMy:::::  :::yMd:::::   yMN:   `dd  :Nd.  `-yMo   oMy   `mN-        ")
print(blu3 + " .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/           oMy   `MMyyyyyy+.      yM:          yM:       `NN-         mMdyyyyy+.    `MN` `dN:         ")
print(blu3 + " +yyyyyyyyyyyyyyyyyyyyyyyyy+++yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`         .NN.   -Mm             .Mm          .Mm        /My         `MM`            yM+-mm-          ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyy/   .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.   ydo++yNd-     yMdo//+o+      yM+          oMo        dM-          oMmo//+oo      :MmNy`           ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyy-   `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.    -+o+/.        ./+o++/.     `NN`         `mM.        //            `:+oo+/-      :MN/             ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyo.   `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                            ``:yM/       ``:yM+                                 ``:yNy`              ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyy/    `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                           /ddyo.       :ddyo.                                 :ddy+`                ")
print(blu3 + " yyyyyyyyyyyyyyyyyyy/     oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyy`    `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyy     `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyy/-..-/yyyyyyyyyyyy/-..-/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.     -+/     :+/                               -/-                                         -Md       ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+      oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.     dNM:   yNMy                               mM.                                         yM/       ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+      oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.    :M+My `ydoM+  +y:    -yo    -oydddyo   +yyyMNyyyyy    .+ydddyyy   -y+`+yddy:    .+ydddyNN`       ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:```.:yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.    dm dm.dy`yM.  NN`    yM/   +My-```.-   ...dM+.....  `yMy:``.yM+   +Mdmo-`-NM`  oMy:``.yMy        ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.   :M+ +Mmy `Nd  /My    `NN`   /Mmo:`        .Mm        yM+    `NN`   yMd.   `oo  yMy     mM.        ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo//////////////oyyyy+//////////////yyyyyyyyyyyyy.   dN` `y+  /Mo  yM-    yMy     ./yyNm+      oMo       .Mm     yMy   `NN`        `NM`    oMy         ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.              -yyyy`              :yyyyyyyyyyyy.  :Mo       yM- `MN   -dMM:         .MN`     dM:       .Mm   .yNM/   +My         `MN`  .yNMo         ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:``````````````/yyyy-``````````````+yyyyyyyyyyyy.  oN`      `Nm   yMdydd/dM`  -mdyyyyNy:      /mNyyyy    yMmydd/yM.   mM.          +Nmydm+yM:         ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.   `        ``    `-.`  ``    `..--`           `--.`     `.-`  ``    ``             .-`  ``          ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+.```-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.     +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.     oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                                                                                     ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy`    :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                :yyyyyyy:                                                            ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.    :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                `....-MN.         ``                                                 ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.   `+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                     +My    /Mo/ymdNNo                                               ")
print(blu3 + " yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.   .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.                                     dM:    yMNy-  `MN                                               ")
print(blu3 + " +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-   /yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`                                    -Mm     mMo    `--                                               ")
print(blu3 + " .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/                                     yM+    :Md              `                                        ")
print(blu3 + "  +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`                              .+.  `oMy`    yM/            /NMd`                                      ")
print(blu3 + "  `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-                               /ymmmdy:     `yy`            :dNy`                                      ")
print(blu3 + "   `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-                                                                                                        ")
print(blu3 + "    `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-                                                                                                         ")
print(blu3 + "      /yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+`                                                                                                          ")
print(blu3 + "       .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-                                                                                                            ")
print(blu3 + "         .+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+-                                                                                                              ")
print(blu3 + "           `:oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo/.                                                                                                                ")
print(blu3 + "              `-+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+:`                                                                                                                   ")
print(blu3 + "                   .-/++oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyooooo+/:-.`                                                                                                                       ")
print('\n')
print(l1n3)
print('\n')
print('\n')

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
    sleep=rate
    check=requests.get("https://" + server + "/api/v2/breachedaccount/" + email + "?includeUnverified=true",
                 verify=sslVerify)
    if str(check.status_code) == "404":
        print(OKGREEN + "[✓] " + email + " has not been breached." + ENDC)
        time.sleep(sleep)
        return False
    elif str(check.status_code) == "200":
        print(FAILRED + "[X] " + email + " has been breached!" + ENDC)
        time.sleep(sleep)
        return True
    elif str(check.status_code) == "429":
        print(WARNING + "[!] Rate limit exceeded, server instructed us to retry after " + check.headers['Retry-After'] + " seconds" + ENDC)
        print(WARNING + "    Refer to acceptable use of API: https://haveibeenpwned.com/API/v2#AcceptableUse" + ENDC)
        sleep = float(check.headers['Retry-After'])
        time.sleep(sleep)
        checkAddress(email)
    else:
        print(WARNING + "[!] Something went wrong while checking " + email + ENDC)
        time.sleep(sleep)
        return True

if __name__ == "__main__":
    main()
print('\n')
print('\n')
print(l1n3)
print('\n')
print('\n')