# imports needed to make the program function
import requests
import csv
import sys

def main():
    # User Interface Title
    print ("Welcome to the STOCK PROGRAM" + "\n")

    # Variables which contain the stock dates, prices, and the csv file retrieved from the stockName() function
    stockD, stockP, listContents = stockName()

    # User Interface Menu
    print ("\n" + "Enter e to exit, c to change the company of the stock")
    print ("r to change the range, h to find the highest and lowest stock price in the range")
    print ("and i to find the stock price on a specific date" + "\n")

    # Automtically setting the highest and lowest value for the high low function
    # to everything in the last 20 years, if user doesnt specify range
    lowIndex = 0
    highIndex = len(stockD)-1

    # userRequest input asks the user which operation it wants to do
    userRequest = str(input("Please enter an operation: "))

    # Central while loop, if user types in e in the userRequest the program exits
    while userRequest != "e":

        # If user types in c in userRequest allows them to change the initial stock that they picked earlier
        if userRequest == "c":
            stockD, StockP, listContents = stockName()

            # Allows the user to repeat the same operation or pick a different one
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")

        # If user types in r in userRequest allows them to pick a date range they want to find the highest, and lowest
        # closing price between those two dates
        elif userRequest == "r":
            lowIndex, highIndex = between(stockD)
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")

        # If user types in i in userRequest allows them to find the price of a stock on a single day
        elif userRequest == "i":
            print (IndivualPrice(stockD, stockP))
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")

        # If user types in c in userRequest allows them to get the highest, and lowest closing price between the date
        # range they picked
        elif userRequest == "h":

            # sortP is a list with the sorted price values from the date range given by the user
            sortP = highLow(stockP, lowIndex, highIndex)
            lowP = 0
            highP = 0

            # for loop searches through the listContents starting from the index of the beginning position of the date
            # range given, to the ending position of the date range given
            for i in range(lowIndex, highIndex):

                #if statements find the date that corresponds to the highest, and lowest closing price
                if str(listContents[i][4]) == str(sortP[0]):
                    lowP = i
                if str(listContents[i][4]) == str(sortP[-2]):
                    highP = i

            #prints out the highest, and lowest closing price for the date given
            print (f'The stock was highest on {listContents[highP][0]} at ${float(sortP[-2]):.2f}')
            print (f'The stock was lowest on {listContents[lowP][0]} at ${float(sortP[0]):.2f}')
            userRequest = input("\n" + "Next operation or x to repeat the operations: ")

        # If user types in x in userRequest allows them to repeat an operation if they made a mistake
        elif userRequest == "x":
            print ("\n" + "Enter e to exit, c to change the company of the stock")
            print ("r to change the range and i to find the stock price on a specific date" + "\n")
            userRequest = input("Next operation: ")

        # error handling if the user types in an operation which is not valid
        else:
             userRequest = input("Please enter a valid operation: ")

    # exits the program once the user types in e
    sys.exit()


# finding stock function
def stockName():

    # user inputs a stock symbol
    stockSymbol = input("Please enter a stock symbol: ")

    # parallel arrays made for the date, and price
    stockD = []
    stockP = []

    # api key to access the api database
    API_KEY = "FO14N65DAE1QVV9A"

    # api url
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockSymbol}&outputsize=full&apikey={API_KEY}&datatype=csv"

    # sends out a request to get the data from the api database formatted into a comma separated value file format
    response = requests.get(url)
    contents = response.text
    listContents = list(csv.reader(contents.splitlines()))

    # for loop made to put data like date, and price into parallel arrays
    for i in range(1, len(listContents)):
        date = listContents[i][0]
        price = listContents[i][4]

        stockD.append(date)
        stockP.append(price)

    # returns the data back to wherever this function is called
    return stockD, stockP, listContents

# function to find the date range based on user preference
def between(stockD):

    # asks user for a starting and ending date
    stockDate1 = str(input("Please enter the older date in the format yyyy-mm-dd: "))
    stockDate2 = str(input("Please enter the latest date in the format yyyy-mm-dd: "))

    # boolean variables setup for error handling
    dateCheck1 = True
    dateCheck2 = True

    # while loop will stop once dateCheck1 becomes false
    while dateCheck1 != False:
        # for loop made to check whether the date exists or not, or is not a weekend
        for i in range(0,len(stockD)-1):
            # if the starting date exists while loop turns false and stops recording the date into the input
            if (str(stockD[i]) == stockDate1):
                dateCheck1 = False
        # if starting date is not valid, while loop doesn't stop and the date is asked again
        if dateCheck1 == True:
            stockDate1 = str(input("\n" + "Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the older date: "))

    # while loop will stop once dateCheck2 becomes false
    while dateCheck2 != False:
        # for loop made to check whether the date exists or not, or is not a weekend
        for i in range(0,len(stockD)-1):
            # if the ending date exists, while loop turns false and stops, recording the date into the input
            if (str(stockD[i]) == stockDate2):
                dateCheck2 = False
        # if starting date is not valid, while loop doesn't stop and the date is asked again
        if dateCheck2 == True:
            stockDate2 = str(input("\n" + "Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the latest date: "))

    # variables to store the index of the two dates above is initialized
    lowIndex = 0
    highIndex = 0

    # for loop made to find the index of the starting, and ending date
    for i in range(1, len(stockD)-1):
        if stockD[i] == stockDate1:
            highIndex = i
        elif stockD[i] == stockDate2:
            lowIndex = i

    # switches the index value if the starting date is bigger then the ending date
    if lowIndex > highIndex:
        i = highIndex
        highIndex = lowIndex
        lowIndex = i

    # returns the index of the date range
    return lowIndex, highIndex

# function made to find the closing price of a stock on a single day
def IndivualPrice(stockD, stockP):

    # asks user for the date they would like to see the closing price for
    dateInput = str(input("In the format yyyy-mm-dd, please enter the date you would like the stock price for : "))

    # boolean setup for error handling
    dateCheck = True

    # while loop will stop once dateCheck becomes false
    while dateCheck != False:
        # for loop made to check whether the date given by the user exists or not
        for i in range(0,len(stockD)-1):
            # if the date exists, while loop turns false and stops, returning the price on the specified date
            if (str(stockD[i]) == dateInput):
                return (f'The stock price on {stockD[i]} was ${float(stockP[i]):.2f}')

                # if the date is not valid, while loop doesn't stop and the date is asked again
        dateInput = str(input("Either you entered a date that falls on a weekend or its not in the format yyyy-mm-dd" +"\n" "Please re-enter the date: "))


# Bubble sort function made to sort the stock price
def highLow(stockP, start, end):

    # contents of stockP copied into new list stockSort
    stockSort = []
    for i in range(start, end):
        stockSort.append(stockP[i])

    # for loop made to through the entire stockSort array
    for i in range(0, len(stockSort) - 1):
        temp = stockSort[i]
        temp2 = i - 1
        while (temp2 >=0) and (float(stockSort[temp2]) > float(temp)):
            stockSort[temp2 + 1] = stockSort[temp2]
            temp2 = temp2 - 1
        stockSort[temp2 + 1] = temp
    return stockSort

main()
