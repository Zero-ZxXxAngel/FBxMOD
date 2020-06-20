#!usr/bin/python2.7
# coding=utf-8

import requests
import sys
import time
import random

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\t\t\033[1;91m____________     ___  ______________ \033[1;91m
\t\t\033[1;91m|  ___| ___ \    |  \/  |  _  |  _  \ \033[1;91m
\t\t\033[1;91m| |_  | |_/ /_  _| .  . | | | | | | | \033[1;91m
\t\t\033[0m|  _| | ___ \ \/ / |\/| | | | | | | | \033[1;91m
\t\t\033[0m| |   | |_/ />  <| |  | \ \_/ / |/ / \033[1;91m
\t\t\033[0m\_|   \____//_/\_\_|  |_/\___/|___/ \n\033[1;91m
\t\t\033[1;97mSCRIPT HACK FB FROM INDONESIA 🇮🇩 🇮🇩 '''

        def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
