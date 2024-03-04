from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
from ..GoogleSheetsIntegration import * 

class Dashboard(DashboardTemplate):   
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        #self.dash_transaction_repeating.items = GoogleSheets
        self.init_components(**properties)
        print(GoogleSheetsIntegration.GetData(2['TransactionID']))
        self.lbl_test.text = GoogleSheetsIntegration.GetData(2['TransactionID'])
        # Any code you write here will run before the form opens.
