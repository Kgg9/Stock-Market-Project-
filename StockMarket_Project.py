import requests
import csv
import datetime
from dateutil import parser


api = "NFMJUNH4NTFPI183"
stock = input("Please Enter In The Stock You Would Like To See The Closing Dates For: ")
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

## try catch error made to catch if the user puts the invalid format of the date
while True:
    try:
        startD = parser.parse(input("Enter The Starting Date In YY MM DD: ")).date()
        endD = parser.parse(input("Enter The Ending Date In YY MM DD: ")).date()
        if startD > endD:
            startD, endD = endD, startD
        break
    except ValueError:
        print("Unrecognized Formatting Of Date Entered, Please Try Again")






# binary search used since it is faster because default python list.index() uses linear search
def binaryS(dateInput, start, end):
    # list doesn't need to be sorted since it is already sorted in descending order

    if start > end:
        return "invalid date please type in date again"

    mid = (start + end) // 2

    if (dateInput == parser.parse(stockD[mid]).date()):
        return mid
    elif(dateInput < parser.parse(stockD[mid]).date()):
        return binaryS(dateInput,mid+1,end)
    elif (dateInput > parser.parse(stockD[mid]).date()):
        return binaryS(dateInput,start,mid-1)


startDIndx = binaryS(startD,0,len(stockD)-1)
endDIndx = binaryS(endD,0,len(stockD)-1)

print(startDIndx)
print(endDIndx)

# Use the index of the start, and end date to make one of the sorting functions to find the highest and lowest price, don't worry about recursion
# already got that with binary search

