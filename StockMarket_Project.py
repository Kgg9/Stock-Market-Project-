import requests
import csv
import sys

def main():
    print ("Welcome to the STOCK PROGRAM")
    stockSymbol = input("Please enter a stock symbol: ")
    stockDetails, listContents = stockName(stockSymbol)
    print ("\n" + "Enter e to exit, c to change the company of the stock")
    print ("r to change the range and i to find the stock price on a specific date")
    userRequest = str(input("Please enter an operation: "))
    while userRequest != "e":
        if userRequest == "c":
            stockSymbol = input("Please enter a stock symbol: ")
            stockDetails, listContents = stockName(stockSymbol)
            userRequest = input("Next operation: ")
        elif userRequest == "r":
            stockDate1 = str(input("Please enter the older date in the format yyyy-mm-dd: "))
            stockDate2 = str(input("Please enter the latest date in the format yyyy-mm-dd: "))
            stockDetails = between(listContents, stockDate1, stockDate2)
            userRequest = input("Next operation: ")
        else:
             userRequest = input("Please enter a valid operation: ")
    sys.exit()

def stockName(stockSymbol):
    stockDetails = {}
    API_KEY = "FO14N65DAE1QVV9A"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockSymbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
    response = requests.get(url)
    contents = response.text
    listContents = list(csv.reader(contents.splitlines()))
    for i in range(1, (len(listContents)-1)):
        stockDetails[listContents[i][0]] = listContents[i][4]
    return stockDetails, listContents

def between(listContents, keyLow, keyHigh):
    lowIndex = 0
    highIndex = 0
    newDic = {}
    for i in range(1, len(listContents)-1):
        if listContents[i][0] == keyLow:
            highIndex = i
        elif listContents[i][0] == keyHigh:
            lowIndex = i
    for i in range(lowIndex, highIndex-1):
        newDic[listContents[i][0]] = listContents[i][4]
    return newDic

main()
