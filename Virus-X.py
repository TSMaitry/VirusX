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
print ("\033[44m                     Welcome To Virus-X                     \033[0m")
print ("\033[44m                     Author: Trilok Singh                   \033[0m")
print

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
  elif dr == "virus-x update":
    print ""+G+"~ "+B+"UPDATING..."
    time.sleep(2)
    print ""+G+"Cloning repo..."
    time.sleep(6)
    os.system("cd ..;rm -rf Virus-X;git clone https://github.com/TSMaitry/Virus-X;cd Virus-X;python2 Virus-.py")
    main()
if __name__ == "__main__":
	main()
  
