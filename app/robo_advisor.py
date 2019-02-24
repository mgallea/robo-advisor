from dotenv import load_dotenv
import json
import os
import requests
import pandas
import datetime

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
	symbol = symbol.upper()

	if not symbol.isalpha():
		print("Whoops! You need to enter a valid stock ticker. Please try again.")
	else:
		timeSeries=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+api_key)
		if "Error" in timeSeries.text:
			print("Whoops! You need to enter a valid stock ticker. Please try again.")
		else:
			break

#Convert the output into JSON for easier access
jsonData = timeSeries.json()

#Pull key information into dictionaries

date = []
openPrice = []
highPrice = []
lowPrice = []
closePrice = []
vol = []


for key, value in jsonData['Time Series (Daily)'].items():
	date.append(key)
	openPrice.append(value['1. open'])
	highPrice.append(value['2. high'])
	lowPrice.append(value['3. low'])
	closePrice.append(value['4. close'])
	vol.append(value['5. volume'])

#Convert dictionaries to Data Frame
dataFrame = pandas.DataFrame({'Date':date,'Opening Price':openPrice, 'Daily High': highPrice,'Daily Low': lowPrice,'Closing Price': closePrice,'Trading Volume': vol})

#Get the Date
today = datetime.datetime.now()
fullDate = today
year = str(today.year)
month = str(today.month)
day = str(today.day)
today = year + "-" + month + "-" + day + "__"

#Convert Data Frame to CSV
dataFrame.to_csv(today + symbol + '.csv')
print("")
print("Your results have been saved successfully.")

#Prepare Output Data
latestDate = date[0]
highestPrice = highPrice[0]
highestPrice = highestPrice[:-2]
lowestPrice = lowPrice[0]
lowestPrice = lowestPrice[:-2]
closingPrice = closePrice[0]
closingPrice = closingPrice[:-2]
openingPrice = openPrice[0]
openingPrice = openingPrice[:-2]

#Print Information
print("")
print("----------------------------------------------------")
print("Stock Symbol: " + symbol )
print("Analysis run at: " + str(fullDate))
print("Latest Date of Available Data: " + latestDate)
print("The Daily High price on " + latestDate + " was:  $" + highestPrice)
print("The Daily Low  price on " + latestDate + " was:  $" + lowestPrice)
print("The opening  price   on " + latestDate + " was:  $" + openingPrice)
print("The closing  price   on " + latestDate + " was:  $" + openingPrice)









exit()
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
