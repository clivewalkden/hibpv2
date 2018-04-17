#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is the installer for hibp.py

import os

print("Installing the HaveIBeenPwned command line interface...")
os.system("chmod +x hibp.py")
print("...")
print("...")
print("...")
print("Thanks for installing the HaveIBeenPwned command line interface! You may use hibp --help to view the help screen!")
os.system("alias hibp='python ~/hibpv2/hibp.py' && rm -rf setup.py")
print("")
