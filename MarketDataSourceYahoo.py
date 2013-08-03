#!/usr/bin/python

from ystockquote import *

class MarketDataSourceYahoo:
	def __init__(self):
		pass

	def getMarketData(self, symbol, start, end):
		return get_historical_prices(symbol, start, end)

if __name__ == '__main__':
	from pprint import pprint
	o = MarketDataSourceYahoo()
	pprint(o.getMarketData('SPY', '20061201', '20130701'))
