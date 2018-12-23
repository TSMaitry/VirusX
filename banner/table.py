#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')

print 
print ("00. Android Bootlop\n")
print ("01. Android Freeze\n")
print ("02. Android Rans\n")
print ("03. Android Malware\n")
print ("04. Android Decryptor\n")
print ("05. Android Decryptor 2\n")
print ("06. Android SMS Tief\n")
print ("07. Android Dangerous Malware\n")
print ("08. Android ENC Malware\n")
print ("09. Android Door Trojan\n")
print ("10. "+R+"EXIT\n")
print 
