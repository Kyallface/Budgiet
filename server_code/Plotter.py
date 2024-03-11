import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import pandas as pd


@anvil.server.callable
def getDataFrame(data): 
    dataframe = pd.DataFrame.from_dict(data.rows)
    