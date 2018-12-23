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
print ("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print ("┃00.        Android Bootlop        ┃")
print ("┃01.        Android Freezen        ┃")
print ("┃02.         Android Ransn         ┃")
print ("┃03.        Android Malware        ┃")
print ("┃04.       Android Decryptor       ┃")
print ("┃05.       Android Decryptor2      ┃")
print ("┃06.        Android SMS Tief       ┃")
print ("┃07.   Android Dangerous Malware   ┃")
print ("┃08.      Android ENC Malware      ┃")
print ("┃09.      Android Door Trojan      ┃")
print ("┃10.           "+R+"EXIT               ┃")
print ("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
print
