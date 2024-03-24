import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import pandas as pd
import plotly.express as px 


@anvil.server.callable
def getDataFrame(data): 
# Get an iterable object with all the rows in my_table
# For each row, pull out only the data we want to putinto pandas
    dicts = [{'Date': r['date'], 'Expense': r['expense'], 'Value': r['value'], 'Catagory': r['catagory']}
         for r in data]
    df = pd.DataFrame.from_dict(dicts)
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    # Convert 'Value' column to numeric after removing pound symbols
    df['Value'] = df['Value'].str.replace('£', '').astype(float)
    return df

@anvil.server.callable
def getCatagoryPlot(importData, datestart, dateend):
    dFrame = getDataFrame(importData)
    dFrame = dFrame[(dFrame['Date'] >= datestart) & (dFrame['Date'] <= dateend)]


    #print(dFrame.head())
    category_totals = dFrame.groupby('Catagory')['Value'].sum().reset_index()
    #print(category_totals)
    catagoryPlot = px.pie(category_totals, values='Value', names='Catagory')

    return catagoryPlot
    
    
