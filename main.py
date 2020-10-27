#!/usr/bin/python3

import urllib.request
import xmltodict

url = 'https://www.oxfordlearnersdictionaries.com/wotd/wotdrss.xml'

word_list = ['']

req = urllib.request.Request(url)
req.add_header('User-agent', 'Mozilla/5.0')

with urllib.request.urlopen(req) as f:
  data = xmltodict.parse(f.read().decode('utf-8'))
  for word in data['feed']['entry']:
    word_list.append(word['title'])

print('Oxford - Word of the day:{}'.format('\n\t'.join(word_list)))
