#!/usr/bin/env python

import requests

url = "ipdestino.com"
req = requests.get(url)

if req.cookies:
	print req.cookies
	cookies = dict(admin='True')
	cookie_req = requests.post(url, cookies=req.cookies, auth=('bee', 'bug'))
	print 'Estado de cookie autenticado:', cookie_req.cookies
	
if req.cookies == cookie req.cookies:
	print 'Identificação da vulnerabilidade de fixação de sessão'