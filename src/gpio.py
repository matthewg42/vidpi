#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import logging

log = logging
log.basicConfig(format='%(asctime)-15s %(message)s', level=logging.INFO)

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)
started = None

try:
    print "PIR Module Test (CTRL+C to exit)"
    while True:
        if GPIO.input(PIR_PIN):
            if started is None:
                started = time.time()
                log.info('motion: STARED')
            else:
                log.debug('motion: CONTINUED')
        else:
            if started is not None:
                log.info('motion: ENDED, duration was %.1f' % (time.time() - started))
                started = None
            else:
                log.debug('motion: nope')
        time.sleep(0.1)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()

