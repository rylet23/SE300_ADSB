import sqlite3
import time
import json as js

# added for postgre DB
import psycopg2
import psycopg2.extras
import os
dbname1 = 'ADBSE300'
user1= 'postgres'
password1 = 'Ryle7953'
host1 = 'localhost'


#Include APISHI//planeapi.json when running within full system
file_path = 'APISHI//planeapi.json'
with open(file_path, 'r') as JSONfile:
    tickers_data = js.load(JSONfile)
    con = psycopg2.connect(dbname=dbname1, user=user1, password=password1, host=host1)
curr = con.cursor()

def ADB():
    count = 0

    for item in tickers_data.values():
        count+=1
        print(item + count)
        try:
            curr.execute('''INSERT INTO ADBSE300 (squawk, alt_geom, adsb_icao, hex, alt_baro, gs, track, baro_rate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (squawk, alt_geom, adsb_icao, hex, alt_baro, gs, track, baro_rate))
            con.commit()

                
        except Exception as e:
            print(f"Error processing {item}: {str(e)}")
            raise

while True:
    curr.execute('DROP TABLE IF EXISTS ADBSE300')
    curr.execute('CREATE TABLE ADBSE300 (squawk TEXT PRIMARY KEY, alt_geom REAL, adsb_icao REAL, hex REAL, alt_baro REAL, gs REAL, track REAL, baro_rate REAL)')
    ADB()

else:
    still_work = input("Outside trading hours, do you still want to execute?(yes or no)? ")
    if still_work == 'yes':
        curr.execute('DROP TABLE IF EXISTS StockInfo1')
        curr.execute('CREATE TABLE ADB (Ticker TEXT PRIMARY KEY, Price REAL, Open_Price REAL, Yesterday_Price REAL, Day_Ago_Price REAL, Delta_Today REAL, Delta_Yesterday REAL, Delta_Total REAL)')
        stocktable()
        print("After hours information displayed.")
    else:
        print("Okay")
