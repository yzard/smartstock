#!/usr/bin/python

import httplib2
from bs4 import BeautifulSoup

class SymbolSourceEOD:
	def __init__(self):
		self.link = 'http://eoddata.com/stocklist/USMF/'
		self.rang = range(ord('A'), ord('Z')+1)

	def getSymbols(self):
		allSymbols = list()
		for i in self.rang:
			l = self.link + chr(i) + '.htm'
			print 'processing: ', l
			content = self._getHtml(l)
			symbols = self._parseSymbols(content)
			allSymbols.extend(symbols)
		return allSymbols

	
	def _getHtml(self, link):
		try:
			h = httplib2.Http()
			response, content = h.request(link, 'GET',)
			return content
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		
	
	def _parseSymbols(self, content):
		data = list()
		soup = BeautifulSoup(content)
		p = soup.find('table', {'class' : 'quotes'})
		s = p.find('tr')
		lines = s.findNextSiblings('tr')
		for line in lines:
			fund = dict()
			symbol = line.find('td')
			cells = symbol.findNextSiblings('td')
			fund['sym'] = str(symbol.text)
			fund['des'] = str(cells[0].text)
			data.append(fund)
		return data


# unit test
if __name__ == '__main__':
	from pprint import pprint
	c = SymbolSourceEOD()
	pprint(c.getSymbols())
