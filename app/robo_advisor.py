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

#Print Information
print("")
print("----------------------------------------------------")
print("Stock Symbol: " + symbol )
print("Analysis run at: " + str(fullDate))
print("Latest Date of Available Data: " + latestDate)
print("The Daily High price on " + latestDate + " was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Daily High'])))
print("The Daily Low  price on " + latestDate + " was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Daily Low'])))
print("The opening  price   on " + latestDate + " was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Opening Price'])))
print("The closing  price   on " + latestDate + " was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Closing Price'])))

#Recomendation








