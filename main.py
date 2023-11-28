import mysql.connector
from mysql.connector import errorcode
import csv


db= mysql.connector.connect(
    user= 'root',
    password= 'W@2915djkq#',
    host= 'localhost',
    database= 'client'
)
cursor = db.cursor()

# CSV file path
csv_file_path = r"C:\Users\diego\OneDrive\Documentos\curso de python\data science\weather.csv"
csv_data = csv.reader(open(csv_file_path))
header = next(csv_data)

print('importing file...')
for row in csv_data:
    print(row)
    cursor.execute('INSERT INTO client (date, city, temperature, humidity) VALUES (%s,%s,%s,%s)', row)

db.commit()
cursor.close()
print('Done')
