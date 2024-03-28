from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import plotly.graph_objects as go
from .. import GoogleSheetsIntegration as gSheet
from .. import DateConverter as dConverter
from .. import GPTIntegration as gpt
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
        #Get the values for the purpose of intiial dating on the data 
        dataStartDate = dConverter.getStartDate(self.dash_year_drop.selected_value, self.dash_month_drop.selected_value)
        dataEndDate = dConverter.getEndDate(self.dash_year_drop.selected_value, self.dash_month_drop.selected_value)
        
        
        self.init_components(**properties)
        #Setup the table of transations
        #Get all of the googlesheet data
        
        
        DatedData = gSheet.GetDatedData(dataStartDate, dataEndDate)
        self.dash_transaction_repeating.items = sorted(DatedData, key=lambda row:row['Date'])
        
        

        #Setup the category plot 
        #Call the method to setup the plot using the start and end dates
        self.dash_category_plot.figure=anvil.server.call('getCatagoryPlot', transaction_data.rows, dataStartDate, dataEndDate)

        #Setup the Float Plot
        self.dash_float_plot.figure=anvil.server.call('GetFloatPlot', transaction_data.rows,dataStartDate, dataEndDate)

        self.Mascot_text_area1.text = gpt.get_Message()



       