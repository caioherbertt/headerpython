# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
import hashlib

user_agents = {'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36 : Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36 : Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}

responses = {}
for name, agent in user_agents():
	headers = {'User-Agent' : agent}
	req = requests.get('http://www.google.com', headers=headers)
	responses[name] = req

md5s = {}

for name, response in responses.items():
	md5s[name] = hashlib.md5(response.text.encode('utf-8')).hexdigest()

for name, md5 in md5s.iteritems():
	if md5 != md5s['Chrome on Windows 8.1']:
                print (name, 'differs from baseline')
