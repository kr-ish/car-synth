#!/usr/bin/env bash

sudo rfcomm release 0
sudo rfcomm bind 0 00:1D:A5:00:02:DA

sudo sh bluetooth.sh 00:1D:A5:00:02:DA
