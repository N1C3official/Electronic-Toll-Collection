
import csv
import matplotlib.pyplot as mt

csvfile1 = open("medal.csv","r")
rowList = csv.DictReader(csvfile1)

countries = {}

for row in rowList:
    if row['country'] in countries:
          countries[row['country']]=countries[row['country']]+1
    else:
          countries[row['country']]=1
print(countries)

data = []
for row in countries:
     data.append(countries[row])
print(mt)

labels = 'I','AU','US','CH'
colors = ['blue','yellow','green','red']
e=(0,0,0,0)

mt.pie(data,explode=e,labels=labels,colors=colors,startangle=90)
mt.axis('equal')
mt.show()
