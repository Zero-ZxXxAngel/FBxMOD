#!usr/bin/python2.7
# coding=utf-8

import os, time
from src import language
from src import follow_me
from src import comment_me
import time
import sys
import random,hashlib,re,threading,json,urllib,datetime
import ConnectionError
import ThreadPool
import browser

def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)

CorrectUsername = "Selaa"
CorrectPassword = "Zero"

loop = 'true'
while (loop == 'true'):
            os.system('clear')
            jalan('\033[1;93mfor your username and password you will be transferred automatically')
    username = raw_input("\033[1;91m>> \x1b[1;91mUsername \x1b[1;91m>> \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m>> \x1b[1;91mPassword \x1b[1;91m>> \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #SCRIPT FROM INDONESIA
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mPassword Salah"
            os.system('xdg-open https://www.instagram.com/zero_xvip')
    else:
        print "\033[1;94mUsername Salah"
        os.system('xdg-open https://www.instagram.com/zero_xvip')


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
