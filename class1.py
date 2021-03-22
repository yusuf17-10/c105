import csv 
import math
f=open("class1.csv",newline="")
reader=csv.reader(f)

data=list(reader)


data.pop(0)
total=0
n=len(data)
for new_data in data :
    total+=float(new_data[1])

mean=total/n

print(mean)

squared_list=[]

for new_data in data :
    a=float(new_data[1])-mean
    a=a**2
    squared_list.append(a)

sum=0

for j in squared_list :
    sum+=j

result=sum/(n-1)

standard_deviation=math.sqrt(result)

print(standard_deviation)


import pandas as pd
import plotly.express as px

df=pd.read_csv("class1.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.show()
