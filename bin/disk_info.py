#!/usr/bin/env python

from pySMART import Device
import sys

dev = sys.argv[1]

info_type = sys.argv[2]
info = ""

device = Device(dev)

if info_type == 'model':
    info = device.model
elif info_type == 'serial':
    info = device.serial
elif info_type == 'is_ssd':
    info = device.is_ssd
elif info_type == 'capacity':
    info = device.capacity
elif info_type == 'assessment':
    info = device.assessment
elif info_type == 'interface':
    info = device.interface
elif info_type == 'messages':
    info = device.messages

print info
