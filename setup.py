#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is the installer for hibpv2

import os

blu3 = '\033[94m'
l1n3 = (blu3 + "<===============================================================================================================>")

print('\n')
print(l1n3)
print('\n')

print("Installing the HaveIBeenPwned command line interface...")
os.system("shred -fuz -n 99 setup.py")
os.system("alias hibp='python ~/hibpv2/hibp.py' >~/.bashrc")
os.system(". ~/.bash_profile")
print("Thanks for installing the HaveIBeenPwned command line interface! You may use hibp --help to view the help screen!")

print('\n')
print(l1n3)
print('\n')