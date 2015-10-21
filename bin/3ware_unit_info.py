#!/usr/bin/env python

import sys
import os

port = sys.argv[1]

info_type = sys.argv[2]
info = ""

if info_type == 'status':
    info = os.popen("/usr/sbin/tw-cli %s show status" % port).read().split(" = ")[1].strip("\n").split(" ")[0]

print info
