from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
from .. import GoogleSheetsIntegration as gSheet


class Dashboard(DashboardTemplate):   
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
         #Load the googlesheet
        transaction_data = gSheet.GetData()

        self.dash_transaction_repeating.items =[
        {'name': 'Alice', 'address': '1 Road Street'},
        {'name': 'Bob', 'address': '2 City Town'}
        ]

      #  [<Google Worksheet Row: {'TransactionID': '1', 'Date': '01/01/2024', 'Expense': 'McDonalds', 'Value': '£17.39', 'Catagory': 'Eating Out'}>, <Google Worksheet Row: {'TransactionID': '2', 'Date': '02/01/2024', 'Expense': 'Tesco', 'Value': '£62.05', 'Catagory': 'Weekly Shop'}>

        self.init_components(**properties)



        # Any code you write here will run before the form opens.
