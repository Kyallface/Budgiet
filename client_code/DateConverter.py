import anvil.server
import anvil.google.auth, anvil.google.drive
import datetime
from anvil.google.drive import app_files
#This module is used to get the start and end dates for calculations 

month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
def getStartDate(year, month):
    month_number = month_dict[month]
    startdate = datetime.datetime(int(year), month_number, 1)
    return startdate.date()

def getEndDate(year, month):
    month_number = month_dict[month]
    startdate = datetime.datetime(int(year), month_number, 1)
    next_month = startdate.replace(day=28) + datetime.timedelta(days=4)
    enddate = next_month - datetime.timedelta(days=next_month.day)
    return enddate.date()
    
