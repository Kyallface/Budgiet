# This module contains the methods needed for the Google sheets integration,
# It can read in the data, add, edit and delete. 
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


#TODO : This needs a try-catch with setup if it is not finding anything
gSheetData = app_files.budgietlinkedsheet 
gWorksheet = gSheetData["Transactions"]

#print the basic information about the spreadsheet to confirm we are loaded correctly 
anvil.server.call('log', gSheetData)
anvil.server.call('log', gWorksheet)
anvil.server.call('log', gWorksheet.fields)
anvil.server.call('log', gWorksheet.row_count)

def GetData(): 
    return gWorksheet

