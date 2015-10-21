Installation Notes
------
```
Clone repo to /opt/zabbix
Install required OS and python packages
Make required edits
```

Required Packages
------
#####OS
```
smartmontools ( confirmed on arch and ubuntu -- requires smartctl 5.42+ )
python-2.7.x
tw-cli ( needed for 3ware userparams and discovery, need to make tw_cli edits )
```

#####Python
```
pysmart
```

Required Edits
------
#####/etc/zabbix/zabbix_agent(d).conf
```
Include=/opt/zabbix/userparams/
EnableRemoteCommands=1
UnsafeUserParameters=1
```

#####/etc/sudoers
```
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/disk_info.p
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/3ware_ctl_discovery.py
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/3ware_info.py
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/3ware_unit_discovery.py
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/3ware_unit_info.py
```
