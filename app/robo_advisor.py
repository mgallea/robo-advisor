from dotenv import load_dotenv
import json
import os
import requests
import pandas
import datetime


#Month Converter // from previous project
def month_converter(monthCode):
	full_month = {'1':'January','2':'February','3':'March','4':'April',
	'5':'May','6':'June','7':'July','8':'August','9':'September','10':'October',
	'11':'November', '12':'December'}
	return full_month[monthCode]

#Retrieve the API Key from the dotenv file
load_dotenv()
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

#Determine stock to track
print("")
print("Welcome to the Robo Advisor Application")
print("---------------------------------------------------------")
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
year = str(today.year)
month = str(today.month)
day = str(today.day)
today = year + "-" + month + "-" + day + "__"

monthFull = str(month)
monthFull = month_converter(month)

#Convert Data Frame to CSV
dataFrame.to_csv(today + symbol + '.csv')
print("")
print("Your results have been saved successfully.")

#Prepare Output Data
latestDate = date[0]

#Get the Month out of the Latest Date
latestMonth = latestDate[5:7]
latestMonth = int(float(latestMonth))
latestMonth = month_converter(str(latestMonth))
print(latestMonth)
latestDay = latestDate[8:10]
latestYear = latestDate[0:4]


#Print Information
print("")
print("---------------------------------------------------------")
print("Stock Symbol: " + symbol )
print("Analysis run on: " + monthFull + " " + day + ", " + year)
print("Latest Date of Available Data: " + latestMonth + " " + latestDay + ", " + latestYear )
print("---------------------------------------------------------")
print("The most recent Recent High price was:  " + "${0:,.2f}".format(max(dataFrame['Daily High'].astype(float))))
print("The most recent Recent Low  price was:  " + "${0:,.2f}".format(min(dataFrame['Daily Low'].astype(float))))
print("The most recent Opening  Price   was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Opening Price'])))
print("The most recent Closing  Price   was:  " + "${0:,.2f}".format(float(dataFrame.iloc[0]['Closing Price'])))
print("---------------------------------------------------------")
#Recomendation
recentLow = min(dataFrame['Daily Low'].astype(float))
recentClose = float(dataFrame.iloc[0]['Closing Price'])

if ((recentClose / recentLow) - 1) < 0.2:
	print("You should buy this stock!")
else:
	print("You should not buy this stock.")
print("---------------------------------------------------------")







