import sqlite3

file_path = r"C:\Users\vs\Downloads\chinook.db"
conn = sqlite3.connect(file_path)
cursor = conn.cursor()
#SQL = """
#SELECT * 
#FROM albums;
#"""
#cursor.execute(SQL)
#results = cursor.fetchall()
#results_list = list(results)  #no need for change to list
#print(results)

import csv
with open (r"C:\Users\vs\Downloads\2022-01-02 (1).csv", "r", encoding="utf-8") as file_obj:
    csv_reader = csv.reader(file_obj)
    data = list(csv_reader)

print(data)
#CREATE_SQL = """
#CREATE TABLE share_data (
#Sno varchar(255),
#symbol varchar(255),
#conf varchar(255),
#open varchar(255)
#);
#"""
#cursor.execute(CREATE_SQL)


INSERT_SQL = """
INSERT INTO share_data(Sno, symbol, conf, open)
VALUES (?,?,?,?) 

"""
cursor.executemany(INSERT_SQL, data)
conn.commit()