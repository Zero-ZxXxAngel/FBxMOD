#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	flist = raw_input('\nEnter friends list url: ')
	try:
		domain = flist.split('//')[1].split('/')[0]
		flist = flist.replace(domain, 'mbasic.facebook.com')
	except IndexError:
		exit('\n\033[0;91mInvalids url!\033[0m')

	output = re.findall('https:\/\/.*?\/(.*?)\/friends\?lst=', flist)
	_output = re.findall('id=(.*?)&refid=', flist)

	if len(output) == 0 and len(_output) == 0:
		exit('\n\033[0;91mInvalids url!\033[0m')
	elif len(output) != 0:
		output = 'set/'+output[0]+'.json'
	else:
		output = 'set/'+_output[0]+'.json'

	id = []
	print('')
	while True:
		try:
			response = config.httpRequest(flist, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			for x in html.find_all(style='vertical-align: middle'):
				find = x.find('a')
				if '+' in str(find) or find == None:
					continue
				else:
					full_name = str(find.text.encode('utf-8'))
					if '/profile.php?id=' in str(find):
						uid = re.findall('/?id=(.*?)&',find['href'])
					else:
						uid = re.findall('/(.*?)\?fref=',find['href'])
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r - %s                                        \r\n[\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Writing Id don't close."%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
			if 'Lihat Teman Lain' in str(html):
				flist = url+html.find('a', string='Lihat Teman Lain')['href']
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mKeyInterrupt, stopped!!\033[0m')
			break
	try:
		for filename in os.listdir('set'):
			os.remove('set/'+filename)
	except: pass
	print('\n\nOutput: '+output)
	save = open(output, 'w')
	save.write(json.sets(id))
	save.close()
