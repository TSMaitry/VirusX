#!/usr/bin/env python

import sys
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

delay_print
delay_print ("\033[;1m Please enter correct number!")
delay_print