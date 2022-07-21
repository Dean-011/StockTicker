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
BZFD_Sh = 4.28
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
        raw_meta_price = float(meta_close_price) * META_Sh
        print("Your total price for META is: $"+str(raw_meta_price))
        time.sleep(30)
        print("Your current portfolio price is: $"+str(raw_meta_price))
        tsla(yesterday,raw_meta_price)
    else:
        print("Error within the API. Ending proccess")
        exit()


def tsla(yesterday, raw_meta_price):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Tesla price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        tsla_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_tsla_price = float(tsla_close_price) * TSLA_Sh
        print("Your total price for TSLA is: $"+str(raw_tsla_price))
        time.sleep(30)
        running_total1 = float(raw_tsla_price) + float(raw_meta_price)
        print("Your current portfolio price is: $"+str(running_total1))
        msft(yesterday,running_total1)
    else:
        print("Error within the API. Ending proccess")
        exit()


def msft(yesterday,running_total1):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Microsoft price yesterday:")
        print(data.get("Time Series (Daily)").get(yesterday1))
        msft_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_msft_price = float(msft_close_price) * MSFT_Sh
        print("Your total price for MSFT is: $"+str(raw_msft_price))
        time.sleep(30)
        running_total2 = float(raw_msft_price) + float(running_total1)
        print("Your current portfolio price is: $"+str(running_total2))
        wmt(yesterday,running_total2)
    else:
        print("Error within the API. Ending proccess")
        exit()


def wmt(yesterday,running_total2):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=WMT&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Walmart price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        wmt_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_wmt_price = float(wmt_close_price) * WMT_Sh
        print("Your total price for WMT is: $"+str(raw_wmt_price))
        time.sleep(30)
        running_total3 = float(raw_wmt_price) + float(running_total2)
        print("Your current portfolio price is: $"+str(running_total3))
        spy(yesterday,running_total3)
    else:
        print("Error within the API. Ending proccess")


def spy(yesterday,running_total3):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("S&P500 price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        spy_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_spy_price = float(spy_close_price) * SPY_Sh
        print("Your total price for SPY is: $"+str(raw_spy_price))
        time.sleep(30)
        running_total4 = float(raw_spy_price) + float(running_total3)
        print("Your current portfolio price is: $"+str(running_total4))
        tlry(yesterday,running_total4)
    else:
        print("Error within the API. Ending proccess")
        exit()


def tlry(yesterday,running_total4):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TLRY&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("Tilray Brands price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        tlry_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_tlry_price = float(tlry_close_price) * TLRY_Sh
        print("Your total price for TLRY is: $"+str(raw_tlry_price))
        time.sleep(30)
        running_total5 = float(raw_tlry_price) + float(running_total4)
        print("Your current portfolio price is: $"+str(running_total5))
        bzfd(yesterday,running_total5)
    else:
        print("Error within the API. Ending proccess")
        exit()


def bzfd(yesterday,running_total5):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BZFD&apikey=UWTP52Z1RRYF3QL9'
    output = requests.get(url)
    data = output.json()
    if data:
        yesterday1 = str(yesterday)
        print("BuzzFeed price yesterday: ")
        print(data.get("Time Series (Daily)").get(yesterday1))
        bzfd_close_price = data.get("Time Series (Daily)").get(yesterday1).get("4. close")
        raw_bzfd_price = float(bzfd_close_price) * BZFD_Sh
        print("Your total price for BZFD is: $"+str(raw_bzfd_price))
        time.sleep(30)
        running_total6 = float(raw_bzfd_price) + float(running_total5)
        print("Your total portfolio price is: $"+str(running_total6))
    else:
        print("Error within the API. Ending proccess")
        exit()
     
main() 