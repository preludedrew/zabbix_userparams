#!/usr/bin/env python
import os, json 



controller = os.popen("sudo /usr/sbin/tw-cli show | grep Ctl -A2 | tail -n1 | awk '{print $1}'").read().strip("\n")

disks = os.popen("sudo /usr/sbin/tw-cli info %s | grep ^p[0-9] | awk '{print$1}'" % controller).read().split("\n")

disks = [i for i in disks if i != '']

data = { "data": [] }

for disk in disks:
    data['data'].append({"{#3WAREDISKNUM}": "/%s/%s" % (controller,disk)})

print json.dumps(data) 
