#!/usr/bin/env python

import sys
import os

port = sys.argv[1]

info_type = sys.argv[2]
info = ""

if info_type == 'model':
    info = os.popen("/usr/sbin/tw-cli %s show model" % port).read().split(" = ")[1].strip("\n")
elif info_type == 'serial':
    info = os.popen("/usr/sbin/tw-cli %s show serial" % port).read().split(" = ")[1].strip("\n") 
elif info_type == 'capacity':
    info = os.popen("/usr/sbin/tw-cli %s show capacity" % port).read().split(" = ")[1].strip("\n").split(" ")
    info = "%s%s" % (info[0], info[1])
elif info_type == 'temperature':
    info = os.popen("/usr/sbin/tw-cli %s show temperature" % port).read().split(" = ")[1].strip("\n").split(" ")[0]
elif info_type == 'status':
    info = os.popen("/usr/sbin/tw-cli %s show status" % port).read().split(" = ")[1].strip("\n").split(" ")[0]

print info
