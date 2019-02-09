```
bluetoothctl

agent on
default-agent
pairable on
disconverable on
scan on
trust [mac]
pair [mac]
exit
```


`sudo rfcomm bind 0 [mac]`

to release:
`sudo rfcomm release 0`