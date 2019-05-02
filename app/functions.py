import locale
import dotenv
import requests

#Convert to USD Format
def to_usd(value):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
        s = locale.currency(value, grouping=True)
        return s

def compile_url(sym , apikey):
	r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+sym+'&apikey='+apikey)
	return r
