import sqlite3
con = sqlite3.connect('country.db')
cur = con.cursor()

data = [(1,'Afghanistan'), (2, 'United Arab Emirates'), (3, 'Bangladesh'), (4, 'Bhutan'), \
        (5, 'China'), (6, 'Germany'), (7, 'France'), (8, 'India'), \
        (9, 'Iran'), (10, 'Iraq'), (11, 'Israel'), (12, 'Kuwait'), \
        (13, 'Monaco'), (14, 'Malaysia'), (15, 'Singapore'), (16, 'Sweden'), \
        (17, 'United States of America')]
cur.execute("create table countries (country_id, country)")
cur.executemany("insert into countries values (?, ?)", data)
cur.execute('select * from countries')
#rows = cur.fetchall()
#for row in rows:
#    print(row) 
con.commit()
cur.close()
con.close()
