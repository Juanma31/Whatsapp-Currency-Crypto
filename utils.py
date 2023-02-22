
import pandas as pd
from twilio.rest import Client
from twilio_Configg import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,WHATSAPP_NUMBER,API_KEY_CURR
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_capi(api_key,currency1,currency2,base_currency):

    url_currency = 'https://api.freecurrencyapi.com/v1/latest?apikey='+api_key+'&currencies='+currency1+'%2C'+currency2+'&base_currency='+base_currency

    try :
        response = requests.get(url_currency).json()
    except Exception as e:
        print(e)

    return response

def get_currency(response):
    currency_eur=response['data']['EUR']
    currency_usd=response['data']['USD']
    
    return currency_eur,currency_usd

def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,query):

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nHello! \n\n\n Today, '+input_date+', the GBP is equal to '+ str(query[0]) + ' EUR and '+ str(query[1])+' AUD',
                        from_=WHATSAPP_NUMBER,
                        to='whatsapp:+447568279452'
                    )

    return message.sid
