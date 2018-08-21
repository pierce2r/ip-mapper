#! /usr/bin/env python 2.x
import requests
import sys
import urllib
import pyperclip
from datetime import datetime

try:
	ip_address=raw_input('Enter IP:')
	main_api = ('https://api.ip2location.com/?ip='+str(ip_address)+'&key=*****&package=WS6') #replace ****** with your API key
	response = requests.get(main_api)

  	print('*'*80)
  	print('Created by Pierce2r').center(80)
	print('Version 1.0').center(80)
  	print('*'*80)
	t1=datetime.now()
	
	if response.status_code==200:
		print('\n[*] Tracking '+str(ip_address)+' for credentials...')
		browser=urllib.urlopen(main_api)
		page=browser.read()
		pyperclip.copy(page)
		paste=pyperclip.paste()
		line=paste.split(';')
		print('[+]Country name: '+line[1])
		print('[+]Region name: '+line[2])
		print('[+]City name: '+line[3])
		print('[+]Latitude: '+line[4])
		print('[+]Longitude '+line[5])
		print('[+]ISP name: '+line[6]+ '\n')
		t2=datetime.now()
		total=t2-t1
		print(total)	
	else:	
		timeout=20
		socket.setdefaulttimeout(timeout)
		print('Connection timeout')

except KeyboardInterrupt:
	sys.exit()

