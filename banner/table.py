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
delay_print ("00. Android Bootlop\n")
delay_print ("01. Android Freeze\n")
delay_print ("02. Android Rans\n")
delay_print ("03. Android Malware\n")
delay_print ("04. Android Decryptor\n")
delay_print ("05. Android Decryptor 2\n")
delay_print ("06. Android SMS Tief\n")
delay_print ("07. Android Dangerous Malware\n")
delay_print ("08. Android ENC Malware\n")
delay_print ("09. Android Door Trojan\n")
delay_print ("10. "+R+"EXIT\n")
print 
