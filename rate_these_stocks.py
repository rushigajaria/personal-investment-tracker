# Install Yahoo Finance https://pypi.python.org/pypi/yahoo-finance

from yahoo_finance import Share
print "Stock Symbols:",
s = raw_input()
companies = map(None, s.split())
# print(len(companies))

stockprices = [[x for x in xrange(2)] for y in range(len(companies))]

i = 0
for company in companies:
	
	information = Share(company)
# 	print(company)
	stockprices[i][0] = company
	volatility = float(information.get_year_high()) - float(information.get_year_low())
	potential = float(information.get_EPS_estimate_next_year()) - float(information.get_earnings_share())
	score = volatility + potential
	stockprices[i][1] = score
	i+=1
	
print sorted(stockprices,key=lambda x: (x[1]), reverse=True)
