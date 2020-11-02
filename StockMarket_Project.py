import requests
import json
import csv

api = "NFMJUNH4NTFPI183"
stock = "IBM"
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock + "&apikey=" + api + "&datatype=csv"

res = requests.get(url)

src = res.text
con = list(csv.reader(src.splitlines()))


datePrice = {}

for i in range(1, len(con)):
    date = con[i][0]
    price = con[i][4]

    datePrice[date] = price

print(datePrice)