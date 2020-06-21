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

K1 = "Zero"
K2 = "ZalasXa"
K3 = "Sumarr-ID"
K4 = "ZxXx-Angel"

loop = 'true'
while (loop == 'true'):
    key1 = raw_input("KEY1==>> ")
    if (key1 == K1):
       key2 = raw_input("KEY2==>> ")
       if (key2 == K2):
          key3 =raw_input("KEY3==>> ")
          if (key3 == K3):
             key4 =raw_input("KEY4==>> ")
             if (key4 == K4):
                jalan ("Selamat datang coo")
                time.sleep(1)
                loop = 'false'
    else:
                jalan ("TOKEN Salah")
                time.sleep(1)
             

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
