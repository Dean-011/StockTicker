from re import T
from unicodedata import decimal
from urllib import response
from datetime import datetime, timedelta, date 
from certifi import where
from decimal import Decimal
import time 
import requests
import json

WMT_Sh = 1.02
SPY_Sh = 0.201808
MSFT_Sh = 0.449768
BSFD_Sh = 4.28
TLRY_Sh = 18.62
TSLA_Sh = 1.16
META_Sh = float(2.67)

def main():
    today = date.today()
    yesterday = today - timedelta(days=1)
    meta(yesterday) 
   #if now.minute >= 30:
        #constructed_time = timedelta(hours=now.hour, minutes=30, seconds=0, microseconds=0)
        #prepped_time = str(today) +" "+ str(constructed_time)
        #print(prepped_time)
        #meta(prepped_time)    
    #else:
        #constructed_time = timedelta(hours=now.hour, minutes=00, seconds=0, microseconds=0)
        #prepped_time = str(today) +" "+ str(constructed_time)
        #print(prepped_time)
        #meta(prepped_time)

def meta(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Meta price yesterday:")
        print(data.get("Time Series (Daily)").get(yesterday1))
        meta_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        my_meta_price = float(meta_close_price) * META_Sh
        print("Your total price for META is: "+str(my_meta_price))
        time.sleep(5)
        tsla(yesterday)
    else:
        print("Error within the API. Ending proccess")
        exit()


def tsla(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Tesla price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        msft(yesterday)
    else:
        print("Error within the API. Ending proccess")
        exit()


def msft(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Microsoft price yesterday:")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        wmt(yesterday)
    else:
        print("Error within the API. Ending proccess")
        exit()


def wmt(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=WMT&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Walmart price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        spy(yesterday)
    else:
        print("Error within the API. Ending proccess")


def spy(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("S&P500 price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        tlry(yesterday)
    else:
        print("Error within the API. Ending proccess")
        exit()


def tlry(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TLRY&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Tilray Brands price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        bzfd(yesterday)
    else:
        print("Error within the API. Ending proccess")
        exit()


def bzfd(yesterday):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BZFD&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("BuzzFeed price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        time.sleep(5)
        calculate()
    else:
        print("Error within the API. Ending proccess")
        exit()





def calculate(my_meta_price):
    print("Your total stock portfolio is : $"+my_meta_price)
    #total_portfolio = my_meta_price
    return





       
main() 