import pandas as pd
import math
import sqlite3

file_name = 'JMP_2021_DEU_Germany.xlsx'
df = pd.read_excel(file_name, sheet_name = 'Water Data', header = [3])
water_data = []
years = df.iloc[:,0].tolist()
years = [x for x in years if pd.isna(x) is False]

fac_type = ['Urban', 'Rural', 'National']

wat_metrics = df.iloc[:,3].fillna('N/A').tolist()
wat_metrics = wat_metrics[0:30]
wat_metrics.insert(0, 'Facility Type')
wat_metrics.insert(0, 'Year')
#wat_metrics = [x for x in wat_metrics if pd.isna(x) is False]
for i in range(len(wat_metrics)):
    if wat_metrics[i] in wat_metrics[0:i]:
        wat_metrics[i] = wat_metrics[i] + ' ' + str(i)
print(wat_metrics)


i = 0 
for (col, colData) in df.iteritems():
    if col[0:5] in fac_type or col[0:8] in fac_type:
        temp = []
        ind = int(math.floor(i/3))
        temp.append(years[ind])
        temp.append(col)
        #print(col)
        #print(colData.values[0:30])
        for j in range(len(colData.values[0:30])):
            if pd.isna(colData.values[j]) is False:
                temp.append(colData.values[j])
            else:
                temp.append('N/A')
        water_data.append(tuple(temp))
        i = i + 1


con = sqlite3.connect('water_germany.db')
cur = con.cursor()
cur.execute('''create table water {}'''.format(tuple(wat_metrics)))
#cur.execute("drop table water")

for i in range(len(water_data)):
    query = 'insert into water values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(query, water_data[i])
    print(i)

cur.execute('select * from water')
#rows = cur.fetchall()
#for row in rows:
#    print(row) 
con.commit()
cur.close()
con.close()


