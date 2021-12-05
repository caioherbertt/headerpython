# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
urls = open("urls.txt", "r")

for url in urls:
	url = url.strip()
	req = requests.get(url)
	print (url, 'report:')
	try:
		xssprotect = req.headers['X-XSS-Protection']
		if xxsprotect != '1; mode=block':
			print ('X-XSS-Protection não está configurado corretamente, pode acontecer um ataque XSS, xssprotect')
	except:
		print ('X-XSS-Protection está configurado corretamente')

	try:
		contenttype = req.headers['X-Content-Type-Options']
		if contenttype != 'nosniff':
			print ('X-Content-Type-Options não está configurado corretamente', contenttype)
	except:
		print ('X-Content-Type-Options está configurado')
	try:
		hsts = req.headers['Strict-Transport-Security']
	except:
		print ('O HSTS header não está configurado, ataques de MITM podem ser possíveis')

	try:
		csp = req.headers['Content-Security-Policy']
		print ('Content-Security-Policy configurado'. csp)
	except:
		print ('Content-Security-Policy não está configurado corretamente')
