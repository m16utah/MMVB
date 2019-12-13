table = pd.DataFrame({'price': pd.Series(range(200000,1000000,25), index=range(200000,1000000,25), dtype='int32'),
                  'volume': 0})
print(table)
# работа с фаилом
with open('C:/Users/User/Desktop/PY/OPEN/csv3.csv', newline = '') as f:
    for row in csv.reader(f, delimiter = ',', quotechar = '"'):
        #перебор свечи
        a=(float(row[6])-(float(row[6])%0.0025))*10000              #редко попадаются не кратные 0.0025 цены
        b=(float(row[5])-(float(row[5])%0.0025)+0.0025)*10000       #диапазон в range, добавляем 0.0025
        for i in range(round(a),round(b),25):
            table.loc[i,'volume'] += 1
        
#===== вывод результата
for i in range(516675,666910,25):
    print (i,",",table.volume[i])
#===== сохраняем в фаил
table.to_csv('C:/Users/User/Desktop/PY/OPEN/output.csv')
