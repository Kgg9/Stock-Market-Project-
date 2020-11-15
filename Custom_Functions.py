import datetime
from dateutil import parser

# custom recursive binary search specialized for date, since it is faster because default python list.index() uses linear search
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
