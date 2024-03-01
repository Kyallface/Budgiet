#Simple logging module as Log is not avaialble in Anvil, set the logging level globally
#Call Logging.log(<Message>) to send a log message, avoids the issue with printing all the time. 

import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import datetime

loggingLevel = 1

@anvil.server.callable
def log (log_message) :
    if loggingLevel == 1: 
        print('DEBUG: ', datetime.datetime.now(), '-', log_message)

