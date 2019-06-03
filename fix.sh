#!/usr/bin/env bash

# Releases and rebinds the OBD reader

sudo rfcomm release 0
sudo rfcomm bind 0 00:1D:A5:00:02:DA

#sudo expect bluetooth.sh 00:1D:A5:00:02:DA
