#!/usr/bin/env python
import os, json 



controller = os.popen("sudo /usr/sbin/tw-cli show | grep Ctl -A2 | tail -n1 | awk '{print $1}'").read().strip("\n")

units = os.popen("sudo /usr/sbin/tw-cli info %s | grep ^u[0-9] | awk '{print$1}'" % controller).read().split("\n")

units = [i for i in units if i != '']

data = { "data": [] }

for unit in units:
    data['data'].append({"{#3WAREUNITNUM}": "/%s/%s" % (controller, unit)})

print json.dumps(data) 
