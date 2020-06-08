import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import os
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits


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
		self.save_dir = self.type_of_file + " " + startime.strftime("%Y-%m-%d %H-%M-%S") + " " + endtime.strftime("%Y-%m-%d %H-%M-%S") + "/"
		self.query_results=[]

	def query(self):
         self.query_results=[]
         for aElem in self.aElements:
             tmp = aElem.text.split('.')[0]
             hhmmss = tmp[-6:]
             yyyymmdd=tmp[-8-6-1:-6-1]
             typ = tmp[4:-8-6-1-1]
             date = datetime(int(yyyymmdd[0:4]),int(yyyymmdd[4:6]),int(yyyymmdd[6:8]),int(hhmmss[0:2]),int(hhmmss[2:4]),int(hhmmss[4:6]))
             if(self.startime<=date<=self.endtime and typ==self.type_of_file):
                 self.query_results.append(aElem.text)
                 return self.query_results

	def get(self):
         if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
            for quer_res in self.query_results:
                urllib.request.urlretrieve(self.URL + quer_res, self.save_dir + quer_res)

	def view(self, filepath):
         image_file = get_pkg_data_filename(filepath)
         fits.info(image_file)
         image_data = fits.getdata(image_file, ext=0)
         plt.figure()
         plt.imshow(image_data,cmap='gray')
         plt.colorbar()

scraper = ScraperXRT('Al_mesh', datetime(2014, 1, 10, 18, 14, 0), datetime(2015, 1, 16, 7, 14, 0))
scraper.query()
scraper.get()
