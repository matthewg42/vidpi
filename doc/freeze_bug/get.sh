#!/bin/bash

scp vidpi:frozen${1?Provide number of log}.log .
ssh vidpi raspi2png
scp vidpi:snapshot.png "screencap$1.png"
