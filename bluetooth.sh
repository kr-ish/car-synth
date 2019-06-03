#!/usr/bin/expect -f

# Pairs bluetooth device at provided MAC address
# Taken from https://gist.github.com/RamonGilabert/046727b302b4d9fb0055

set prompt "#"
set address [lindex $argv 0]

spawn sudo bluetoothctl -a
expect -re $prompt
# send "remove $address\r"
# sleep 1
# expect -re $prompt
# send "scan on\r"
# send_user "\nSleeping\r"
# sleep 5
# send_user "\nDone sleeping\r"
# send "scan off\r"
# expect "Controller"
send "trust $address\r"
sleep 2
send "pair $address\r"
sleep 2
send "1234\r"
sleep 3
send_user "\nShould be paired now.\r"
send "quit\r"
expect eof
