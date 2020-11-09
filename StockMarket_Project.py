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
            print (IndivualPrice(stockD, stockP))
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "h":
            sortP = highLow(stockP, lowIndex, highIndex)
            lowP = 0
            highP = 0
            for i in range(1, len(listContents)):
                if float(listContents[i][4]) == float(sortP[0]):
                    lowP = i
                if float(listContents[i][4]) == float(sortP[-2]):
                    highP = i
            print (f'The stock was highest on {listContents[highP][0]} at ${sortP[-2]}')
            print (f'The stock was lowest on {listContents[lowP][0]} at ${sortP[0]}')
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")
        elif userRequest == "x":
            print ("\n" + "Enter e to exit, c to change the company of the stock")
            print ("r to change the range and i to find the stock price on a specific date" + "\n")
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

def IndivualPrice(stockD, stockP):
    # Implements a binary search with recursion to find the stock price on a date

    dateInput = str(input("In the format yyyy-mm-dd, please enter the date you would like the stock price for : "))
    dateCheck = True

    while dateCheck != False:
        for i in range(0,len(stockD)-1):
            if (str(stockD[i]) == dateInput):
                return (f'The stock price on {stockD[i]} was ${float(stockP[i]):.2f}')
        dateInput = str(input("Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the date: "))

def highLow(stockP, start, end):
    stockSort = []

    for i in range(start, end):
        stockSort.append(stockP[i])

    for i in range(start, end):
        temp = stockSort[i]
        temp2 = i - 1
        while (temp2 >=0) and (float(stockSort[temp2]) > float(temp)):
            stockSort[temp2 + 1] = stockSort[temp2]
            temp2 = temp2 - 1
        stockSort[temp2 + 1] = temp
    return stockSort

main()
