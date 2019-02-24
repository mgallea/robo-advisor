from dotenv import load_dotenv
import json
import os
import requests

#Retrieve the API Key from the dotenv file
load_dotenv()
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

#Determine stock to track
print("")
print("Welcome to the Robo Advisor Application")
print("----------------------------------------------------")
print("")
while True:
	symbol = input("Which stock would you like to retrieve quotes for? ")

	if not symbol.isalpha():
		print("Whoops! You need to enter a valid stock ticker. Please try again.")
	else:
		timeSeries=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+api_key)
		print(timeSeries.text)
		if "Error" in timeSeries.text:
			print("Whoops! You need to enter a valid stock ticker. Please try again.")
		else:
			break

#Convert the output into JSON for easier access
jsonData = timeSeries.json()


latest_price_usd = "$100,000.00"
print("-----------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: 11:52pm on June 5th, 2018")
print("-----------------")
print("LATEST DAY OF AVAILABLE DATA: June 4th, 2018")
print(f"LATEST DAILY CLOSING PRICE: {latest_price_usd}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-----------------")
print("RECOMMENDATION: Buy!")
print("RECOMMENDATION REASON: Because the latest closing price is within threshold XYZ etc., etc. and this fits within your risk tolerance etc., etc.")
print("-----------------")
