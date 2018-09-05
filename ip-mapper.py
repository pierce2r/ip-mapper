import requests
import socket
import sys
import urllib
import pyperclip
from datetime import datetime
try:
	ip_address=raw_input('Enter IP:')
	main_api = ('https://api.ip2location.com/?ip='+str(ip_address)+'&key=******&package=WS6') #replace api with yours
	response = requests.get(main_api)
#banner design
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
		print('[+]Longitude: '+line[5])
		print('[+]ISP name: '+line[6])
		t2=datetime.now()
		total=(t2-t1)
		print('Scan Completed in: ' + str(total))	
	else:	
		timeout=10
		socket.setdefaulttimeout(timeout)
		print('Connection timeout')

except KeyboardInterrupt:
	sys.exit()
