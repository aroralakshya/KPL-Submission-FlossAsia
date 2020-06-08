# all imports below

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import os

class ScraperXRT:
	def __init__(self, typeof_file, startime, endtime):
		self.URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
		self.pageResponse = requests.get(self.URL)
		self.bsParser = BeautifulSoup(self.pageResponse.content, 'html.parser')
		self.trElements = self.bsParser.find_all('tr')
		self.aElements = self.bsParser.find_all('a')[5:]
		self.type_of_file = typeof_file
		self.startime = startime
		self.endtime = endtime
		self.save_dir = self.type_of_file + "/"

	def query(self):
		# for aElem in self.aElements:
		aElem = self.aElements[0]
		tmp = aElem.text.split('_')
		typ = tmp[1] + "_" + tmp[2]
		time = tmp[4].split('.')[0]
		datetime_str = ''.join(tmp[3][0:4]) + '/' + ''.join(tmp[3][4:6]) + '/' + ''.join(tmp[3][6:]) + ' ' + ''.join(time[0:2]) + ':' + ''.join(time[2:4]) + ':' + ''.join(time[4:])
		datetime_object = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M:%S')
		
		print(typ)
		print(tmp[3])
		print(tmp[4])
		print(datetime_str)
		# print(time)

	def get(self):
		os.mkdir(self.save_dir)
		urllib.request.urlretrieve(self.URL + self.aElements[0].text, self.save_dir + self.aElements[0].text)

	def view(self, filepath):
		return NotImplementedError

scraper = ScraperXRT('AI_mesh', datetime.now(), datetime.now())
scraper.query()
# scraper.get()