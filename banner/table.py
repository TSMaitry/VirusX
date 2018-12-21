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
print "▛▀▀▀▀▀▀▜"
print "▌1        ▐"
print "▌2        ▐"
print "▌3        ▐"
print "▌4        ▐"
print "▌5        ▐"
print "▌6        ▐"
print "▌7        ▐"
print "▌8        ▐"
print "▌9        ▐"
print "▌10       ▐"
print "▌exit     ▐"
print "▙▄▄▄▄▄▄▟"
print 
