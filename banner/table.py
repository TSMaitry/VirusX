#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import sys
#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print 
delay_print "01. Android Bootlop"
delay_print "02. Android Freeze"
delay_print "03. Android Rans"
delay_print "04. Android Malware"
delay_print "05. Android Decryptor"
delay_print "06. Android Decryptor 2"
delay_print "07. Android SMS Tief"
delay_print "08. Android Dangerous Malware"
delay_print "09. Android ENC Malware"
delat_print "10. Android Door Trojan"
delay_print "exit"
delay_print 
