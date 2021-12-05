# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests

req = requests.get("https://google.com.br")
headers = ['Server','Date','Via','X-Powered-By']

for header in headers:
	try:
		result = req.headers[header]
		print ('%s: %s' %(header, result))
	except Exception:
		pass
