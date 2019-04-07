import lecturaPreciosAPI
import lecturaNet_Hash_Rate_API
import psycopg2

sql = "SELECT date, price, timestamp FROM bitcoin_prices;"
sql2 = "SELECT fecha, hash_rate, timestamp FROM net_hash_rate;"
sql3 = "INSERT INTO excel_hash_rate (date, bitcoin_price, net_hash_rate) VALUES (%s, %s, %s);"

conn = psycopg2.connect(host="localhost",database="Back y Front End Python", user="adolfo", password="aePOnW8;0c73)LTb")
cur = conn.cursor()
cur.execute(sql)
resul = cur.fetchall()
# print(resul)
cur2 = conn.cursor()
cur2.execute(sql2)
resul2 = cur2.fetchall()
# print(resul2)
lista = []
for i in range(len(resul)):
    date = resul[i][0]
    price = resul[i][1]
    hash_rate = resul2[i][1]
    cur3 = conn.cursor()
    cur3.execute(sql3, (date, price, hash_rate))
    conn.commit()
    print("Grabando ", date, price, hash_rate, " en la base de datos...")
conn.close()
 