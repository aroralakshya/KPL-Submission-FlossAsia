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

	def query(self):
		print(self.trElements[3])
		

	def get(self):
		return NotImplementedError

	def view(self, filepath):
		return NotImplementedError

scraper = ScraperXRT('AI_mesh', datetime.now(), datetime.now())
scraper.query()