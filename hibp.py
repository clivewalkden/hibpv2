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
l1n3=(p1nk + "<===============================================================================================================>")

address = str(args.address)
filename = str(args.filename)
lstEmail = ["info@example.com","example@example.com"]
print('\n')
print('\n')
print('\n')
print(l1n3)
print('\n')
print('\n')
print(blu3 + "                       `-:/+oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+/::.`                                                                                                                                                      ")
print(blu3 + "                  `-/oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+/-`                                                                                                                                                 ")
print(blu3 + "               ./yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo:.                                                                                                                                              ")
print(blu3 + "            ./yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo:`                                                                                                                                           ")
print(blu3 + "          .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/.                                                                                                                                         ")
print(blu3 + "        .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/.                                                                                                                                       ")
print(blu3 + "      `/yhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:`                                                     -/+oo+/`        ./+oo++.                                                        ")
print(blu3 + "     .yyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+.             `yyyyyyyyy/                          +mNdyyyyy       :dNmyyyyy-                                                        ")
print(blu3 + "    :yhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-            .oooooohMM/                         yMm-            :NM+`                                                              ")
print(blu3 + "   :yhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-                  yMN`       ./oyyo/.         -MM/            `dMy         `//` `/oyo+.       `:+oyo/-     :+/       :+/          ")
print(blu3 + "  -yhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-                `NMy      /dNdyyyhNNy   .////yMM/////:`  :///+MMy/////.   :MM:yNhyyhMN:    -hNmyyyyNNh`   +MM-      mMd          ")
print(blu3 + " .yhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`               +MM-    `hMd-`    yMN`  +hhhdMMmhhhhhy` -hhhhNMNhhhhhh-   oMMNy-   `MMy   oNN/`    /MM:   .NMy     /MM:          ")
print(blu3 + " +hhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/               dMd     hMN+:://oyNm+       +MM-            .MM+          hMM+     `/+.  +MMy:::/+yNNy`    yMN`   -NMo           ")
print(blu3 + ".yhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo.             -MM/    -MMhyyyyyo/-`        dMh             +MN.         .NMy            mMmyyyyyo+:`      :MM/  -mMy            ")
print(blu3 + "/hhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyoooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:             hMm`    :MM:                -MM/             mMy          +MN`           `NMy                dMh /NN+             ")
print(blu3 + "yhhhhhhyhhhyyyyyyyyyyyyyyyyyyyy-`   +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+    `yy:.../hMd-     `mMm/-...--:        yMm`            :MM:          mMy             yMN+-....-:`       +MNyNd-              ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyo`    :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+    .ohmmmddy/`       `ohmmmmmddy       `NMy             yMm          -dm-             `/hdmmmmddh`       `MMMy`               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyy/`    :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo      ``..``            ```..```        +MN.            -NM+           ``                 ``..````       .yMm:                 ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyy-     :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                   `.-:yNN/        `..-+mMy                                         ..-:yNmo`                  ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyo.     -yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                   ydddho.         /dddhy:                                          ydddy/.                    ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyo`     -yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                   `.``            `.```                                            `.``                       ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyy.      +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyo       +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyo       +yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                    ``         ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyy-.```.-yyyyyyyyyyyyyyyo/---:/oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo       `---      .--.                                       .-.                                                    +md`        ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy`      .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo       oNNm`    /mNNy                                      -NN:                                                    mMy         ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+        oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo      .NNdM-   +NyMM:   ..`      ..`       .----..     ....yMN-.....       `.----...`    `.`  `.--.`        `.----/MM:         ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo       `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo      oMooMy  oNo/MN`  :mm.     .mm:    `odmdddddd+   `ddddMMNdddddh`    -ydmdddmmmm-    dm+-ydddmNd:    `/ymddddmNMd          ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/.````.+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo     `NN.-Mm`yN+ yMy   yMd      yMm`    hMd-.```..`    ...oMN:......   `yNmo-```.dMd    .NMhmy:.`.dMd   -dMh/.``.:MM+          ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo     oMy  mMhN/ `mM/  .NM+     `mMy    `dMm/.`            dMh          yMm.     .NM+    :MMm:     yhy  .mMy`     +MN`          ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo    .NM-  oNm:  :MN.  oMN`     oMM.     .ydmmmho-        -MM/         -MM/      yMN`    yMN-           yMm`     .mMy           ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-.................:yyyyy+..................:yyyyyyyyyyyyyyyo    oMh   `-.   yMh   mMy     +NMd        `.-/yMN/       oMN`         oMN`    `oMMy    `NMo            mMh     .dMM:           ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                  `oyyyy:                  `yyyyyyyyyyyyyyyo   `NM:        `NM+  .MMo  `-ymNMy    .`     `:MM+       hMm`         +MM:  `:hmMM+    +MN.            dMd`  .+mmMM`           ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.`````````````````-yyyyy+.`````````````````:yyyyyyyyyyyyyyyo   .Md         :MM.   yNNhydmy:NM/   `mddhyyhdmdo`       :mNmhyhh+    `yNNhhdmy:MM-    dMh             -mMdyhdd/oMm            ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyoooooooooooooooooyyyyyyyyyyyyyyyyo   `:.         .::     -/+/:.  ::`    -://++/:-`          `-/++/:.      -/+/-. `::     ::.              `:/+/-` .:-            ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:...../yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/       yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:      `yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                                                                                                               ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:      .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                          `````````                                                                            ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-     `oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                         /hhhhhhddd-                                                                           ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-     `oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                         -::::::dMm`           ``                                                              ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:     -yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo                                               .NMo     :yy .+yhhhy-                                                           ")
print(blu3 + "hhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:    `/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+                                               oMM.     yMdymh+::hMN.                                                          ")
print(blu3 + "yhhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:    `+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+                                              `mMh      mMMd-    /NN-                                                          ")
print(blu3 + "/hhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/    -yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:                                              :MM:     .NMh`     `-.                                                           ")
print(blu3 + ".yhhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+++oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`                                              hMm`     oMN.                                                                    ")
print(blu3 + " +hhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/                                       `      /MM+     `mMy                /yyo`                                                ")
print(blu3 + " `yhhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo`                                      /my+//+yNm+      :MM-               -MMMM/                                                ")
print(blu3 + "  -yhhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo.                                       ./yhddyo:`       /yo                 +hho`                                                ")
print(blu3 + "   -yhhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo-                                                                                                                                  ")
print(blu3 + "    -yhyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo.                                                                                                                                   ")
print(blu3 + "     .oyhhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+`                                                                                                                                    ")
print(blu3 + "       /yhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo:                                                                                                                                      ")
print(blu3 + "        .+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/`                                                                                                                                       ")
print(blu3 + "          .+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo/`                                                                                                                                         ")
print(blu3 + "            `:oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+-`                                                                                                                                           ")
print(blu3 + "               .:oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+:`                                                                                                                                              ")
print(blu3 + "                  `./+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo+:.                                                                                                                                                  ")
print(blu3 + "                       `.-:/+ooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyooyooooooooooooooooooooo++//:-.`                                                                                                                                                      ")
print('\n')
print(l1n3)
print('\n')
print('\n')

print
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
        print(OKGREEN + "[i] " + email + " has not been breached." + ENDC)
        time.sleep(sleep)
        return False
    elif str(check.status_code) == "200":
        print(FAILRED + "[!] " + email + " has been breached!" + ENDC)
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
