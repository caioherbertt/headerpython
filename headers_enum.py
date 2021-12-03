#!/usr/bin/env python
import requests

req = requests.get("http:siteaqui.com.br")
headers = ['Server','Date','Via','X-Powered-By']

for header in headers:
	try:
	result = req.headers[header]
		print '%s: %s' %¨(header, result)
	except Exception, error:
		pass