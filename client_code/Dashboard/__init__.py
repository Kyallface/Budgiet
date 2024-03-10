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
        print (transaction_data.cells)

        self.dash_transaction_repeating.items = transaction_data.cells

        self.init_components(**properties)



        # Any code you write here will run before the form opens.
