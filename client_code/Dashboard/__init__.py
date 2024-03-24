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
        startdate = '2024-02-01'
        endDate = '2024-02-29'
        
        
        
        self.init_components(**properties)
        #Setup the table of transations: 
        self.dash_transaction_repeating.items = transaction_data.rows

        #Setup the category plot 
        self.dash_category_plot.figure=anvil.server.call('getCatagoryPlot', transaction_data.rows, startdate, endDate)
