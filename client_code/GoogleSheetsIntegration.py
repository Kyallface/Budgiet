import anvil.google.auth, anvil.google.drive
import logging
from anvil.google.drive import app_files
# This module contains the methods needed for the Google sheets integration,
# It can read in the data, add, edit and delete. 

#TODO : This needs a try-catch with setup if it is not finding anything
gSheetData = app_files.budgietlinkedsheet 
gWorksheet = gSheetData["Transactions"]

#print the basic information about the spreadsheet to confirm we are loaded correctly 
print(gSheetData)
print (gWorksheet)
print(gWorksheet.fields)

