#!/usr/bin/env python2

import socket, urllib2, sys


type = sys.argv[1]
ip = ""

if type == 'internal':
    ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
elif type == 'external':
    response = urllib2.urlopen("http://www.icanhazip.com")
    ip = response.read().strip("\n")
elif type == 'borenfam':
    ip = socket.gethostbyname("borenfam.com")

print ip
