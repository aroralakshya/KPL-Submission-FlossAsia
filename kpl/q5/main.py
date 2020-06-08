# all imports below

import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ScraperXRT:
	def __init__(self, typeof_file, startime, endtime):
		self.URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
		self.pageResponse = requests.get(self.URL)
		self.bsParser = BeautifulSoup(self.pageResponse.content, 'html.parser')
		self.trElements = self.bsParser.find_all('tr')
		self.aElements = self.bsParser.find_all('a')[5:]

	def query(self):
		# for aElem in self.aElements:
		aElem = self.aElements[0]
		tmp = aElem.text.split('_')
		typ = tmp[1] + "_" + tmp[2]
		date = tmp[3]
		time = tmp[4].split('.')[0]
		print(typ)
		print(date)
		print(time)


	def get(self):
		return NotImplementedError

	def view(self, filepath):
		return NotImplementedError

scraper = ScraperXRT('AI_mesh', datetime.now(), datetime.now())
scraper.query()
# print(datetime.now())