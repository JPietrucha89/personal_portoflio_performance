import sqlite3


#  Define connection and cursor
connection = sqlite3.connect('portfolio.db')

cursor = connection.cursor()

# Create starting table
sql_string = '''
CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)
'''

cursor.execute(sql_string)

# add 3 rows
cursor.execute("INSERT INTO stores VALUES(1, 'Warszawa')")
cursor.execute("INSERT INTO stores VALUES(2, 'Kraków')")
cursor.execute("INSERT INTO stores VALUES(3, 'Radom')")

# get results
sql_string = '''
select * from stores
'''
cursor.execute(sql_string)
results = cursor.fetchall()

print(results)

for result in results:
    print(result)