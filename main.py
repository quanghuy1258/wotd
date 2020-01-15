#!/usr/bin/python3

import urllib.request
import xmltodict

url = 'https://www.oxfordlearnersdictionaries.com/wotd/wotdrss.xml'

word_list = ['']

with urllib.request.urlopen(url) as f:
  data = xmltodict.parse(f.read().decode('utf-8'))
  for word in data['feed']['entry']:
    word_list.append(word['title'])

print('Oxford - Word of the day:{}'.format('\n\t'.join(word_list)))
