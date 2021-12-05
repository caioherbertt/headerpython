# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
verbs = ['GET','POST','PUT','DELETE','OPTIONS','TRACE','TEST']

for verb in verbs:
	req = requests.request(verb, 'http://testeseusite.com.br')
	print (verb, req.status_code, req.reason)
	if (verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text):
		print ('Possivel vulnerabilidade XSS encontrada') 
