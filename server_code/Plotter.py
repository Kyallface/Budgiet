import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import pandas as pd
import plotly.express as px 



@anvil.server.callable
def getDataFrame(data): 
# Get an iterable object with all the rows in my_table
# For each row, pull out only the data we want to put into pandas
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
    datestart = pd.to_datetime(datestart)
    dateend = pd.to_datetime(dateend)
    dFrame = getDataFrame(importData)
    dFrame = dFrame[(dFrame['Date'] >= datestart) & (dFrame['Date'] <= dateend)]  # Parentheses added here

    #print(dFrame.head())
    category_totals = dFrame.groupby('Catagory')['Value'].sum().reset_index()
    #print(category_totals)
    catagoryPlot = px.pie(category_totals, values='Value', names='Catagory')

    return catagoryPlot
    
import pandas as pd
import plotly.express as px


@anvil.server.callable
def GetFloatPlot(importData, startDate, endDate):
    # Convert start and end dates to datetime objects
    startDate = pd.to_datetime(startDate)
    endDate = pd.to_datetime(endDate)
    
    # Get DataFrame
    dFrame = getDataFrame(importData)
    
    # Filter DataFrame based on start and end dates
    dFrame = dFrame[(dFrame['Date'] >= startDate) & (dFrame['Date'] <= endDate)]
    
    # Group by date and calculate the average transaction value for each date
    daily_avg = dFrame.groupby('Date')['Value'].mean().reset_index()
    
    # Create a new column for the running total
    daily_avg['Running_Total'] = 2000 - daily_avg['Value'].cumsum()
    
    # Create a line plot using Plotly Express
    fig = px.line(daily_avg, x='Date', y='Running_Total', title='Running Total of Transactions')
    
    # Return the figure
    return fig