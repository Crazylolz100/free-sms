import os, sys, time, mechanize
from bs4 import BeautifulSoup as sup
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('Connection', 'keep-alive'), ('Pragma', 'no-cache'), ('Cache-Control', 'no-cache'), ('Origin', 'http://sms.payuterus.biz'), ('Upgrade-Insecure-Requests', '1'), ('Content-Type', 'application/x-www-form-urlencoded'), ('User-Agent', 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'), ('Referer', 'http://sms.payuterus.biz/alpha/'), ('Accept-Encoding', 'gzip, deflate'), ('Accept-Language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')]
z = []

def send():
	os.system('clear')
	print('[\x1b[1;92m*\x1b[1;97m] Free Sms [\x1b[1;92m*\x1b[1;97m]')
	print('\x1b[1;91m~\x1b[1;92m Author : Gr3y C0d3rs')
	print('\x1b[1;92m>> https://github.com/Crazylolz100\x1b[0m')
	no = raw_input('[\x1b[1;92m+\x1b[1;97m] Destination Number ex(+62) : ')
	pesan = raw_input('[\x1b[1;92m*\x1b[1;97m] Message : \x1b[0m')
	if pesan =="":
		send()
	else:
		bs = sup(br.open('http://sms.payuterus.biz/alpha'), features='html.parser')
		for x in bs.find_all('span'):
			z.append(x.text)
			
		a = str(z)[3]
		b = str(z)[7]
		snd = raw_input('[\x1b[1;92m#\x1b[1;97m] ' + a + ' + ' + b + ' = ' '\x1b[0m')
		br.select_form(nr=0)
		br.form['nohp'] = str(no)
		br.form['pesan'] = str(pesan)
		br.form['captcha'] = str(snd)
		print('[\x1b[1;92m+\x1b[1;97m] Sending...')
		get = br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(get):
			print('[\x1b[1;92m*\x1b[1;97m] Sended : ') +str(no)
			p = raw_input('[\x1b[1;92m?\x1b[1;97m] Send Again? [y/n] : ')
			if p =="y":
				os.system('python2 free.py')
			else:
				exit()
		else:
			print('[\x1b[1;91m!\x1b[1;97m] Failed To Send : ') +str(no)
			query = raw_input('[\x1b[1;92m?\x1b[1;97m] Send Again? [y/n] : ')
			if query =="y":
				os.system('python2 free.py')
			else:
				exit()
				
send()