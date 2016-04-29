# Configuration Process

1.  Burn the raspbian jessie lite image to an SD card
2.  Have a Pi ready, connected to your local network by ethernet cable
3.  Boot pi with new Raspbian Jessie Lite SD card in it
4.  ping raspberrypi to verify you can see it
5.  run: *make expand* - this will expand the fs, change the hostname, change the password and add an ssh authorized key
6.  run: *make app* - this will update jessie and install all requires software. Warning: this takes a LONG time because it has to build openFrameworks from source and the RPi is not the fastestest system.  On a Pi3 with a class 10 SD card about 1h 30m at time of writing.

