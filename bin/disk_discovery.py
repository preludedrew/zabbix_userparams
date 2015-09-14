#!/usr/bin/env python
import os, json 

disks = os.popen("ls /dev/sd?").read().split("\n")

disks = [i for i in disks if i != '']

data = { "data": [] }


for disk in disks:
    data['data'].append({"{#DISKNAME}": disk})



print json.dumps(data) 
