import sqlite3
import glob
import os
import csv

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

csv_files = glob.glob('*.csv')

for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)

    # Specify the encoding here (replace 'latin-1' with the correct encoding)
    with open(csv_file, 'r', encoding='utf-8') as file:  
        reader = csv.reader(file)
        header = next(reader)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name[0]} ({', '.join(header)})")
        for row in reader:
            cursor.execute(f"INSERT INTO {table_name[0]} VALUES ({', '.join(['?' for _ in row])})", row)

conn.commit()
conn.close()

print("CSV files imported successfully!")
