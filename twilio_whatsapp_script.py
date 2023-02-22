"""
************************************************************************
* Author = @Juanma31                                                   *
* Date = '22/02/2023'                                                  *
* Description = Sending whatsapp messages using Python. Currency       *
************************************************************************
"""


import os
from twilio.rest import Client
from twilio_Configg import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,WHATSAPP_NUMBER,API_KEY_CURR
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import date
from utils import request_capi,get_forecast,create_df,send_message,get_date



base_currency= 'GBP'
currency1='EUR'
currency2='USD'
api_key = API_KEY_CURR

input_date= get_date()
response = request_capi(api_key,currency1,currency2,base_currency)

query=get_currency(response)


# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,query)


print('Mensaje Enviado con exito ' + message_id)
