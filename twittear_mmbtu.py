#!/usr/bin/env python
import argparse
import tweepy
from datetime import datetime
from backports import csv
import sys
import time
import os
import twitter
import io
from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests
from panditas import mmbtu

api_key = 'VVakn3YiVxqxS7vBzhOB4waTi'
api_secret = 'xPuLbI0r0gHME3QaV9lnVh1TQPPxF1rHqZL0MOEs2vr74neg3U'

access_token = '11627302-B7MaD2Cw52blSjPBpEX61fGcOXjBsUCB8wLlFnSi6'
access_token_secret = 'mDS4Ie6JFbrCUgso1HOFelWG2WOAn3ObWFuutfXled6YK'

def escribir(text):
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    text2 = text[0].strftime('%Y-%m-%d') + " Bitcoin Mining Break-Even Index: $" + str(text[1][:4]) + "/mmBtu" 
    api.update_status(text2)
    print("Acabas de publicar el siguiente tweet \n")
    print(text)

escribir(mmbtu(3012)[-1])
print(mmbtu(3012))