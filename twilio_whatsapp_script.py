"""
************************************************************************
* Author = @Juanma31                                                             *
* Date = '25/02/2023'                                                            *
* Description = Sending whatsapp messages using Python. Currency & Crypto.       *
************************************************************************
"""


import os
from twilio.rest import Client
from twilio_Configg import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,WHATSAPP_NUMBER,API_KEY_CURR,API_KEY_CRYP,MY_WHATSAPP_NUMBER
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import date
from utils import request_capi,get_currency,send_message,get_date,request_crypapi,get_cryptos,create_df_crypto



base_currency= 'GBP'
currency1='EUR'
currency2='USD'
api_key = API_KEY_CURR
api_crypto=API_KEY_CRYP

input_date= get_date()

#Currency
response = request_capi(api_key,currency1,currency2,base_currency)

query=get_currency(response)

#Cryptos
data=request_crypapi(api_crypto)
data_crypto = []

for i in tqdm(range(10),colour = 'green'):
    
    data_crypto.append(get_cryptos(data,i))
    
df_crypto=create_df_crypto(data_crypto)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,query,df_crypto)


print('Message sent succesfully ' + message_id)
