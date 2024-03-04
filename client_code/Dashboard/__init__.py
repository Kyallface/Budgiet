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
        #self.dash_transaction_repeating.items = GoogleSheets
        self.init_components(**properties)
        transaction_data = gSheet.GetData(2['TransactionID'])
        print(transaction_data)
        self.lbl_test.text = transaction_data
        # Any code you write here will run before the form opens.
