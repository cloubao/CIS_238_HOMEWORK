#!/usr/bin/python

import os

myuid = os.getuid()

if myuid == 0:
    print "You are root" 

elif myuid < 500:
    print "You are a system account"

else: 
    print "You are just a regular user"