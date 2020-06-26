#!usr/bin/python2.7
# coding=utf-8
#The Credit For This Code Goes To Rana Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os, time
from app4 import config
from app4 import login
from app4 import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser
import time
import sys
import random



def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.05)

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu += ('  \033[1;90m[ 1 ]  Start Crack\n')
		self.menu += ('  \033[1;90m[ 2 ]  DM Id Friends\n')
		self.menu += ('  \033[1;90m[ 3 ]  DM Id by Search name\n')
		self.menu += ('  \033[1;90m[ 4 ]  DM Id from likes status\n')
                self.menu += ('  \033[1;90m[ 5 ]  DM id Friends lists\n')
                self.menu += ('  \033[1;90m[ 7 ]  Update Script?\n')
		self.menu += ('  \033[1;90m[ 0 ]  Remove cookies\n')
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[1;90m[WARNING] Cookies invalids, please login again.\033[1;90m')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		jalan('\033[1;90m      ________________________________________________________')
		jalan('\t\t\n\033[1;90m                  (\033[0;90m•\033[1;90m)  BY: Zero & Sumarr ID  \033[1;90m(\033[0;90m•\033[1;90m)')
		jalan('\033[1;90m      ________________________________________________________')
                print(' ')
                jalan('\t\t\t\033[1;93m(☠☠☠☠☠ SERVER)')
		print(self.menu)
		try:
			choose = int(raw_input('\033[1;90m Selaa>===>># '))
		except ValueError:
			exit('\n\033[1;90mYou Crazy.\033[1;90m')
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
                        os.system('clear')
                        jalan('\033[1;90mPlease Wait !')
		        os.system('git pull origin master')
		        raw_input('\n\x1b[1;90m[ \x1b[1;90mBack \x1b[1;90m]')
		        exit()
		elif choose == 0:
			ask = raw_input('\nAre you Sure? [y/N]:\033[1;90m ')
			if ask.lower() == 'y':
				jalan('\nRemoving cookies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				jalan('\n\033[1;90mSuccess removed!\033[1;90m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\ncanceled!')
				self.start()
		else: exit('\n\033[1;90mYou crazy.\033[90m')
