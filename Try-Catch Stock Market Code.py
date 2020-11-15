import requests
import csv
import datetime
from dateutil import parser
from Custom_Functions import*

choice = input("\nHello Welcome To The Stock Market Program, Press:\n1 To Find The Stock \n3 To Exit The Program\n")

while (choice!="3"):

    if (choice=="1"):

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

    choice = input("\nHello Welcome To The Stock Market Program, Press:\n1 To Change The Stock\n2 To Find/Change The Date Range\n3 To Exit The Program")

    if (choice == "2"):
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
                rangedStockD = stockD[endDIndx:startDIndx + 1]

                highStockP= (selectionSort(rangedStockP, 0, len(rangedStockP)-1)[0])
                lowStockP = (selectionSort(rangedStockP, 0, len(rangedStockP)-1)[-1])


                print(f"The Highest Closing Price Was ${highStockP} And Was On {rangedStockD[rangedStockP.index(highStockP)]}")
                print(f"The Lowest Closing Price Was ${lowStockP} And Was On {rangedStockD[rangedStockP.index(lowStockP)]}")

                break

            except:
                print("The Date You Have Entered Is Invalid, Please Try Again, Also Remember The Stock Market Is Closed On The Weekends")
