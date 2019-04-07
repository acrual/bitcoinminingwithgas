import urllib.request
import json
from datetime import datetime, timedelta
import time
import psycopg2

url = 'http://192.168.1.45:5002/net_hash_rate'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

sql = "INSERT INTO excel_hash_rate (id, date, computer_capacity, net_hash_rate, bitcoins_per_month, bitcoins_per_computer, bitcoin_price, usd_per_computer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
res = response(url)
datos = json.loads(res)['Net_Hash_Rate']
conn = psycopg2.connect(host="localhost",database="Back y Front End Python", user="adolfo", password="aePOnW8;0c73)LTb")
i = -1
# for i in range(len(datos)):
data = (datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6], datos[i][7])
cur = conn.cursor()
cur.execute(sql, data)
conn.commit()
print("Grabando ", data)

conn.close()