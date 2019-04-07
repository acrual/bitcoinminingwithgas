import urllib.request
import json
from datetime import datetime, timedelta
import time
import psycopg2
# from config import Config

url = 'https://api.blockchain.info/charts/market-price?timespan=all&format=json'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

sql =  "INSERT INTO bitcoin_prices (Date, Price, Timestamp) VALUES (%s, %s, %s);"

res = response(url)
conn = psycopg2.connect(host="localhost",database="Back y Front End Python", user="adolfo", password="aePOnW8;0c73)LTb")
sql2 = "SELECT Date, Price, Timestamp FROM bitcoin_prices ORDER BY Date DESC LIMIT 1"
cur = conn.cursor()
cur.execute(sql2)
resul = cur.fetchone()
print(resul)
print(type(resul[2]))
for value in json.loads(res)['values']:
        if value['x'] > resul[2]:
                print("Fecha es: ", datetime.utcfromtimestamp(value['x']).strftime('%d/%m/%Y'), "y precio de bitcoin ", value['y'], "Timestamp es: ", value['x'])
                value1 = datetime.utcfromtimestamp(value['x']).strftime('%d/%m/%Y')
                value2 = value['y']
                value3 = value['x']
                data = (value1, value2, value3)
                # execute a statement
                cur = conn.cursor()
                cur.execute(sql, data)
                # commit the changes to the database
                conn.commit()
conn.close()

# PENDIENTE: seleccionar última fecha con dato en la tabla de la bbdd y rellenar desde ahí



