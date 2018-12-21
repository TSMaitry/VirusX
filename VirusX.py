#!/usr/bin/evn python

import sys
import os
import time
import os as sistema

# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
os.system("cd banner;python2 banner4.py")
print
print ("\033[49m                     Welcome To Virus-X                     \033[0m")
print ("\033[48m                     Author: Trilok Singh                   \033[0m")
print

os.system("cd banner;python2 table.py")

def help():
  print
  print ("\033[44m Hi \033[0m")
  print ("\033[44m Hello\033[0m")
  print ("\033[44m Hi\033[0m")
  print
  main()

def main():
  dr = raw_input(">>> ")
  if dr == "show options":
    time.sleep(1)
    help()
    main()
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
  elif dr == "virusx update":
    delay_print (""+G+"~ "+B+"UPDATING...")
    time.sleep(1)
    delay_print (""+G+"Cloning repo...")
    time.sleep(1)
    os.system("cd ..;rm -rf VirusX;git clone https://github.com/TSMaitry/VirusX;cd VirusX;python2 VirusX.py")
    main()
if __name__ == "__main__":
	main()
  
