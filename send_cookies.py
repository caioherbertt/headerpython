# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests

url = "http://facebook.com"
req = requests.get(url)

if req.cookies:
	print (req.cookies)
	cookies = dict(admin='True')
	cookie_req = requests.post(url, cookies=req.cookies, auth=('bee', 'bug'))
	print ('Estado de cookie autenticado:', cookie_req.cookies)

if req.cookies == cookie_req.cookies:
	print ('Identificação da vulnerabilidade de fixação de sessão')
