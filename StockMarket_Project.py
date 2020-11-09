import requests
import csv
import sys

sys.setrecursionlimit(5982)

def main():
    print ("Welcome to the STOCK PROGRAM" + "\n")
    stockD, stockP, listContents = stockName()
    print ("\n" + "Enter e to exit, c to change the company of the stock")
    print ("r to change the range, h to find the highest and lowest stock price in the range")
    print ("and i to find the stock price on a specific date" + "\n")
    lowIndex = 0
    highIndex = len(stockD)-1
    userRequest = str(input("Please enter an operation: "))

    while userRequest != "e":
        if userRequest == "c":
            stockD, StockP, listContents = stockName()
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "r":
            lowIndex, highIndex = between(stockD)
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "i":
            IndivualPrice(stockD, stockP, lowIndex, highIndex)
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "h":
            highLow(stockP, lowIndex, highIndex)
            low = 0
            high = 0
            for i in range(0, len(listContents) - 1):
                if listContents[i][4] == stockP[0]:
                    low = i
                if listContents[i][4] == stockP[-1]:
                    high = i
            print (f'The stock was highest on {listContents[low][0]} at ${stockP[-1]}')
            print (f'The stock was lowest on {listContents[high][0]} at ${stockP[0]}')
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "x":
            print ("\n" + "Enter e to exit, c to change the company of the stock")
            print ("r to change the range and i to find the stock price on a specific date")
            userRequest = input("Next operation: ")
        else:
             userRequest = input("Please enter a valid operation: ")
    sys.exit()

def stockName():
    stockSymbol = input("Please enter a stock symbol: ")
    stockDetails = {}
    stockD = []
    stockP = []
    API_KEY = "FO14N65DAE1QVV9A"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockSymbol}&outputsize=full&apikey={API_KEY}&datatype=csv"
    response = requests.get(url)
    contents = response.text
    listContents = list(csv.reader(contents.splitlines()))
    for i in range(1, len(listContents)):
        date = listContents[i][0]
        price = listContents[i][4]

        stockD.append(date)
        stockP.append(price)
    return stockD, stockP, listContents

def between(stockD):
    stockDate1 = str(input("Please enter the older date in the format yyyy-mm-dd: "))
    stockDate2 = str(input("Please enter the latest date in the format yyyy-mm-dd: "))
    dateCheck1 = True
    dateCheck2 = True

    while dateCheck1 != False:
        for i in range(0,len(stockD)-1):
            if (str(stockD[i]) == stockDate1):
                dateCheck1 = False
        if dateCheck1 == True:
            stockDate1 = str(input("\n" + "Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the older date: "))

    while dateCheck2 != False:
        for i in range(0,len(stockD)-1):
            if (str(stockD[i]) == stockDate2):
                dateCheck2 = False
        if dateCheck2 == True:
            stockDate2 = str(input("\n" + "Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the latest date: "))

    lowIndex = 0
    highIndex = 0
    newDic = {}
    temp = ""

    for i in range(1, len(stockD)-1):
        if stockD[i] == stockDate1:
            highIndex = i
        elif stockD[i] == stockDate2:
            lowIndex = i
    if lowIndex > highIndex:
        i = highIndex
        highIndex = lowIndex
        lowIndex = i

    return lowIndex, highIndex

def IndivualPrice(stockD, stockP, start, end):
    # Implements a binary search with recursion to find the stock price on a date

    dateInput = str(input("In the format yyyy-mm-dd, please enter the date you would like the stock price for : "))
    dateCheck = True

    while dateCheck == True:
        for i in range(0,len(stockD)-1):
            if (stockD[i] == dateInput):
                print (f'The stock price on {stockD[i]} was ${float(stockP[i]):.2f}')
        if dateCheck == True:
            stockDate = str(input("Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the date: "))

def highLow(stockP, start, end):
    part = partition(stockP, start, end)
    if (part - 1) > start:
	     highLow(stockP, start, part-1)
    if (part + 1) < end:
	     highLow(stockP, part+1, end)
    
    return stockP

def partition(stockP, start, end):
    pivot = float(stockP[start])
    for i in range(start, end):
        if (float(stockP[i]) < pivot):
            temp = float(stockP[start])
            stockP[start] = i
            stockP[i] = temp
            start += 1;

    temp = float(stockP[start])
    stockP[start] = pivot
    stockP[end] = temp

    return start

main()
