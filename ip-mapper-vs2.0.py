import requests
import socket
import sys
import urllib
import pyperclip
import webbrowser
import time
from datetime import datetime
try:
	ip_address=raw_input('Enter IP:')
	main_api = ('https://api.ip2location.com/?ip='+str(ip_address)+'&key=*******&package=WS6') #replace api with yours
	response = requests.get(main_api)
#banner design
  	print('*'*80)
  	print('Created by Pierce2r').center(80)
	print('Version 2.0').center(80)
  	print('*'*80)
	t1=datetime.now()	
	if response.status_code==200:
		print('\n* Connecting to satellite...')
		time.sleep(4)
		print('[*] Tracking '+str(ip_address)+' for credentials...')
		time.sleep(4)
		print('[*] Narrowing search...')
		time.sleep(3)
		print('[*] Locating '+ str(ip_address))
		time.sleep(3)
		print('[*] Target found\n')
		time.sleep(2)
		browser=urllib.urlopen(main_api)
		page=browser.read()
		pyperclip.copy(page)
		paste=pyperclip.paste()
		line=paste.split(';')
		longitude=line[5]
		latitude=line[4]		
		city=line[3]
		region=line[2]
		country=line[1]
		print('[+]Country name: '+line[1])
		print('[+]Region name: '+line[2])
		print('[+]City name: '+line[3])
		print('[+]Latitude: '+line[4])
		print('[+]Longitude: '+line[5])
		print('[+]ISP name: '+line[6])
		t2=datetime.now()
		total=t2-t1
		print('Scan Completed in: ' + str(total))
		print('[*]Scanning for 3D view...')
		time.sleep(2)
		web=webbrowser.open('https://www.google.com/maps/place/'+str(city)+','+str(region)+','+str(country)+'/@'+str(latitude)+','+str(longitude))
	
	else:	
		timeout=10
		socket.setdefaulttimeout(timeout)
		print('Connection timeout')

except KeyboardInterrupt:
	sys.exit()
