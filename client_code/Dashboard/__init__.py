from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
from .. import GoogleSheetsIntegration as gSheet
from .. import DateConverter as dConverter
import datetime


class Dashboard(DashboardTemplate):   
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
         #Load the googlesheet
        transaction_data = gSheet.GetAllData()
        
        #Setup the Dropdowns
        self.dash_year_drop.items = ['2024', '2025','2026']
        self.dash_month_drop.items = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'September', 'October', 'November', 'December']
        self.dashboard_period_drop.items = ['1','2','3','4']
        #Get the current Date
        today=datetime.datetime.now()
        print(today)
        #Set the default value on the dropdowns to today
        self.dash_year_drop.selected_value = str(today.year)
        self.dash_month_drop.selected_value = datetime.datetime.strftime(today, "%B")
        
        
        self.init_components(**properties)
        #Setup the table of transations: 
        self.dash_transaction_repeating.items = transaction_data.rows
        self.dash_transaction_repeating.
        

        #Setup the category plot 
        plotStartDate = dConverter.getStartDate(self.dash_year_drop.selected_value, self.dash_month_drop.selected_value)
        plotEndDate = dConverter.getEndDate(self.dash_year_drop.selected_value, self.dash_month_drop.selected_value)
        self.dash_category_plot.figure=anvil.server.call('getCatagoryPlot', transaction_data.rows, plotStartDate, plotEndDate)



       