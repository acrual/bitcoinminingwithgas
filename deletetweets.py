#!/usr/bin/env python
import argparse
import tweepy
from datetime import date
from backports import csv
import sys
import time
import os
import twitter
import io
from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests

api_key = 'VVakn3YiVxqxS7vBzhOB4waTi'
api_secret = 'xPuLbI0r0gHME3QaV9lnVh1TQPPxF1rHqZL0MOEs2vr74neg3U'

access_token = '11627302-B7MaD2Cw52blSjPBpEX61fGcOXjBsUCB8wLlFnSi6'
access_token_secret = 'mDS4Ie6JFbrCUgso1HOFelWG2WOAn3ObWFuutfXled6YK'

def delete(api, date, r):
    with io.open("tweets.csv", encoding='utf-8') as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int(row["tweet_id"])
            tweet_date = parse(row["timestamp"], ignoretz=True).date()

            if date != "" and tweet_date >= parse(date).date():
                continue

            if (r == "retweet" and row["retweeted_status_id"] == "" or
                    r == "reply" and row["in_reply_to_status_id"] == ""):
                continue

            try:
                print("Borrando tweet #{0} ({1})".format(tweet_id, tweet_date))

                api.DestroyStatus(tweet_id)
                count += 1


            except twitter.TwitterError as err:
                print("Excepción: %s\n" % err.message)

    print("Number of deleted tweets: %s\n" % count)

def escribir(text):
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(api_key, api_secret) 

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    api.update_status(status=text)
    print("Acabas de publicar el siguiente tweet \n")
    print(text)

def read(usuario): 
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    user = api.get_user(usuario)
    # print("num seguidores", user.followers_count, user.friends()[0])
    user_tweets = api.user_timeline()
    for tweet in user_tweets:
        if tweet.text[2] == '-' and tweet.text[6] == '-':
            lista = (tweet.text).split(' ')
            cifra = lista[len(lista) - 1]
            return cifra

def ult_tweets(usuario):
    listado = []
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    user = api.get_user(usuario)
    # print("num seguidores", user.followers_count, user.friends()[0])
    user_tweets = api.user_timeline()
    for tweet in user_tweets:
        listado.append(tweet.text)
    return listado


def amiguitos(usuario):
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    user = api.get_user(usuario)
    listado = []
    # print("num seguidores", user.followers_count)
    page_count = 0
    ids = []
    """ for page in tweepy.Cursor(api.followers_ids, screen_name=usuario).pages():
        ids.extend(page)
        time.sleep(60) """
    # print(len(ids))
    for friend in user.friends():
        listado.append(friend.screen_name)
    return listado

def sacar(usuario):
    url = 'https://twitter.com/'+usuario
    # print("url es ", url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    # print("soup es ", soup)
    try:
        f = soup.find('li', class_="ProfileNav-item--followers")
        s = soup.find('li', class_="ProfileNav-item--following")
        # print("f es ", f)
        title = f.find('a')['title']
        title2 = s.find('a')['title']
        # print(title)
        num_followers = int(title.split(' ')[0].replace('.',''))
        num_siguiendo = int(title2.split(' ')[0].replace('.',''))
    except:
        return "no disponible"
    return num_followers, num_siguiendo

def purge(usuario):
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    tweets = api.favorites(usuario)
    for f in tweets:
        api.destroy_favorite(f.id)
        time.sleep(0.1) # wait 6 seconds between requests to avoid rate limit.

def error(msg, exit_code=1):
    sys.stderr.escribir("Error: %s\n" % msg)
    exit(exit_code)

def main():
    parser = argparse.ArgumentParser(description="Delete old tweets.")
    parser.add_argument("-d", dest="date", required=True,
                        help="Delete tweets until this date")
    parser.add_argument("-r", dest="restrict", choices=["reply", "retweet"],
                        help="Restrict to either replies or retweets")

    args = parser.parse_args()
    todo = input("Quieres amiguitos, escribir, borrar, sacar datos, leer, eliminar likes?(a/e/b/s/l/eli) ")
    if todo == "b":
        api = twitter.Api(api_key, api_secret, access_token, access_token_secret)
        delete(api, args.date, args.restrict)
    elif todo == "e":
        text = input("Dime el texto que quieres escribir: ")
        escribir(text)
    elif todo == "l":
        user = input("dime usuario: ")
        read(user)
    elif todo == "s":
        f = open('trackedusers.txt')
        line = f.readline()
        if read('acrual') != None:
            dato_anterior = int(read('acrual'))
        else:
            dato_anterior = 0
        # print("esto es ", line.replace(' ', ''))
        print(line, sacar(line.strip()))
        suma = 0
        while line:
            line = f.readline()
            line = line.strip()
            # print("tipo suma", type(suma))
            # print("tipo sacar", type(sacar(line)[0]))
            if type(sacar(line)[0]) == int:
                suma = suma + sacar(line)[0]
            print("suma es ",suma)
            print(line, "seguidores", sacar(line)[0], "siguiendo ",sacar(line)[1])
            if sacar(line)[0] == 'n' and sacar(line)[1] == 'o':
                twittear = False
            else:
                twittear = True
        texto = "Selected bitcoin twitter follower count: "
        growth = suma - dato_anterior
        if growth > 0:
            res = "positive"
        else:
            res = "negative"
        print(date.today().strftime('%d-%b-%Y'), texto, suma, growth)
        g = open('temp.txt', 'w')
        if twittear == True:
            g.write("\n" + "Extremely simple bitcoin price predictor: " + "\n" + date.today().strftime('%d-%b-%Y') + " growth: " + str(growth) + " is " + res + "\n" + texto + str(suma))
        else:
            print("Sorry, hay varios de baja...")
        g.close()
        g = open('temp.txt', 'r')
        escribir(g.read())
        g.close()
        f.close()
    elif todo == "eli":
        i = 1
        while True:
            print("borrando like número ", i)
            purge("@acrual")
            i += 1
    elif todo == "a":
        user = input("dime usuario: ")
        amiguitos(user)
        
    else:
        print("vuelve a intentarlo")

if __name__ == "__main__":
    main()