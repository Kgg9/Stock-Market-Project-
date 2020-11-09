import requests
import csv
import datetime
from dateutil import parser
from Custom_Functions import*

print("Welcome To The Stock Market Program")


while True:
    try:
        api = "NFMJUNH4NTFPI183"
        stock = input("\nPlease Enter In The Stock You Would Like To See The Closing Dates For: ")
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock + "&apikey=" + api + "&datatype=csv"

        res = requests.get(url)

        src = res.text
        con = list(csv.reader(src.splitlines()))

        stockD = []
        stockP = []


        for i in range(1, len(con)):
            date = con[i][0]
            price = con[i][4]

            stockD.append(date)
            stockP.append(price)
        break
   # IndexError setup for list, since if the stock enterted is not valid the list would be out of bounds since there
   # would be nothing to put in there
    except IndexError:
        print("Please Enter A Valid Stock")

## try catch error made to catch if the user puts the invalid format of the date, or if the user enters the weekend date
while True:
    try:
        print(f"\nClosing Prices Available From {stockD[-1]} to {stockD[0]}\n")

        startD = parser.parse(input("Enter The Starting Date In YY MM DD: ")).date()
        endD = parser.parse(input("Enter The Ending Date In YY MM DD: ")).date()

        if startD > endD:
            startD, endD = endD, startD

        startDIndx = binarySDate(stockD, startD, 0, len(stockD) - 1)
        endDIndx = binarySDate(stockD, endD, 0, len(stockD) - 1)

        rangedStockP = stockP[endDIndx:startDIndx + 1]

        break

    except:
        print("The Date You Have Entered Is Invalid, Please Try Again, Also Remember The Stock Market Is Closed On The Weekends ")

print(rangedStockP)


# Ask if we need to have a ui since it would make the code harder to read, and more complicated for no reason
# if we do make the ui bruh
# something like this
# already made all of the try catches
# print("\nHello Welcome, Press:\n1 To Change The Stock\n2 To Change The Date Range\n3 To Exit The Program")


#First sort the rangedStockP using any sorting method we learnd its up to you man, won't be able to help since i'm really sick
# also put the sorting function in the custom_functions.py it makes our main less cluttered
# once the sorting is done get the highest and lowest value from the sort

# once you got those two values use the custom binarySPrice function to find there index which then corresponds to the date
# its in the custom functions if it doesn't work let me know

# binarySPrice(stockPrice, highValueNum, 0, len(stockPrice)-1) = index number of the highest closing value in the stockPrice array
# binarySPrice(stockPrice, lowValueNum, 0, len(stockPrice)-1) = index number of the lowest closing value in the stockPrice array

# then just print this to finish it off
# print(f"the highest closing price was on {stockDate[highIndxNum]} with its price being {stockDate[highIndxNum]})
