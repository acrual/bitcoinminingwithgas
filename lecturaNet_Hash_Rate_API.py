import urllib.request
import json
from datetime import datetime
import psycopg2

url = 'https://api.blockchain.info/charts/hash-rate?timespan=all&format=json'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

sql =  "INSERT INTO net_hash_rate (fecha, hash_rate, timestamp) VALUES (%s, %s, %s);"

res = response(url)
conn = psycopg2.connect(host="localhost",database="Back y Front End Python", user="adolfo", password="aePOnW8;0c73)LTb")
sql2 = "SELECT fecha, hash_rate, timestamp FROM net_hash_rate ORDER BY fecha DESC LIMIT 1;"
cur = conn.cursor()
cur.execute(sql2)
resul = cur.fetchone()
print(resul)
if resul != None:
        print(type(resul[2]))
        timestamp = resul[2]
else:
        timestamp = 0
for value in json.loads(res)['values']:
        if value['x'] > timestamp:
                print("Fecha es: ", datetime.utcfromtimestamp(value['x']).strftime('%d-%b-%Y'), "hash_rate ", value['y'], "timestamp: ", value['x'])
                value1 = datetime.utcfromtimestamp(value['x']).strftime('%d-%b-%Y')
                value2 = value['y']
                value3 = value['x']
                data = (value1, value2, value3)
                # execute a statement
                cur = conn.cursor()
                cur.execute(sql, data)
                # commit the changes to the database
                conn.commit()
conn.close()

