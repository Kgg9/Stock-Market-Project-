import datetime
from dateutil import parser

# custom binary search specialized for date, since it is faster because default python list.index() uses linear search
def binarySDate(stockDateArray,dateInput, start, end):
    # list doesn't need to be sorted since it is already sorted in descending order

    if start > end:
        return "invalid date please type in date again"

    mid = (start + end) // 2

    if (dateInput == parser.parse(stockDateArray[mid]).date()):
        return mid
    elif(dateInput < parser.parse(stockDateArray[mid]).date()):
        return binarySDate(stockDateArray,dateInput,mid+1,end)
    elif (dateInput > parser.parse(stockDateArray[mid]).date()):
        return binarySDate(stockDateArray,dateInput,start,mid-1)



    # custom function for finding the index number of the highest and lowest closing price
def binarySPrice(stockPriceArray,priceInput, start, end):
    # list doesn't need to be sorted since it is already sorted in ascending order

    if start > end:
        return "invalid date please type in date again"

    mid = (start + end) // 2

    if (priceInput == parser.parse(stockPriceArray[mid]).date()):
        return mid
    elif(priceInput > parser.parse(stockPriceArray[mid]).date()):
        return binarySPrice(stockPriceArray,priceInput,mid+1,end)
    elif (priceInput < stockPriceArray[mid]):
        return binarySPrice(stockPriceArray,priceInput,start,mid-1)