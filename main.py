import sqlite3

conn = sqlite3.connect('first_sql.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# SELECT
cursor.execute('select count(*) from song_details where language <> "English"')
result = cursor.fetchall()
list_results = [list(row) for row in result]
for row in list_results:
    print(row)

cursor.execute('select count(*) from (select distinct genre from song_details)');
result = cursor.fetchall()
list_results = [list(row) for row in result]
for row in list_results:
    print(row)

# UPDATE
cursor.execute('''update song_details
set song_length_seconds = 180
where year = 2018;''')
cursor.connection.commit()
cursor.execute('select * from song_details');
result = cursor.fetchall()
list_results = [list(row) for row in result]
for row in list_results:
    print(row)

conn.close()
