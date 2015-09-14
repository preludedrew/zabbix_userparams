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
zabbix ALL=(ALL) NOPASSWD: /opt/zabbix/bin/disk_info.py 
```
