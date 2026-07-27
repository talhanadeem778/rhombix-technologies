import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "name":["talha" , "nadeem" , "rafey" , "asghar", "sara" , "ali" , "ahmed" ,"tahir" ,"abdullah" , "saifullah" , "mirza" , "alisha" , "baig" , "osama","usama" , "ali tahir" , "danish" , "moeen" , "sarim" , "anas"],
    "gender":["male" , "male", "male", "male", "female", "male", "male", "male", "male", "male", "male", "female", "male", "male", "male" , "male", "male", "male", "male", "male"],
    "percentage":[73,45,67,23,45,67,88,22,11,45,78,98,45,55,34,45,56,67,88,98],
    "attendence_percentage":[34,56,55,44,67,21,56,78,43,56,77,65,76,44,56,87,89,32,11,44],
    "curricular_activities":["yes","yes","no","yes","no","yes","yes","no","yes","no" , "yes","yes","no","yes","yes","no","yes","yes","no","no"],
    "grade":["A","C" , "B" , "D" , "np.nan" , "C" , "B","C" , "A" , "C" , "F" , "C" , "D" , "E" , "B" , "C","D","F","C","C"]
    })
print(df)

print(" drop function used")
print("drop " , df.dropna(), "\n")
print(df.dropna())

fill = df.fillna("B")
print(fill)

print("Missing values:\n", df.isna(), "\n")
print("Missing values:\n", df.notna(), "\n")

print(df.replace("nadeem" , "azhar"))

print(df["name"].str.strip())


print(df['gender'].str.lower())


print(df['curricular_activities'].str.upper())

s = df.sort_values(by='name', ascending=True)
print("after sort" , s , "\n")

t= s.sort_values(by='percentage', ascending=True)
print("after sort" ,t , "\n")

u = t.sort_values(by='attendence_percentage', ascending=True)
print("after sort" ,u ,"\n")

drop = u.drop_duplicates("name")
print("after drop duplicates",drop , "\n")

drop = drop.drop_duplicates("percentage")
print("after drop duplicates",drop , "\n")

d = drop.drop_duplicates("attendence_percentage")
print("after drop duplicates",d ,"\n")


e = d.clip()
print(e)


#data is cleaned
#task 02
#statistical function apply on upper dataset
mean = e[["id" ,"percentage" , "attendence_percentage"]].mean()
print("mean is","\n",mean)

mode= e[["id" ,"percentage" , "attendence_percentage"]].mode()
print("mod is","\n",mode)

var = e[["id" ,"percentage" , "attendence_percentage"]].var()
print("var is","\n",var)

std= e[["id" ,"percentage" , "attendence_percentage"]].std()
print("std is","\n",std)

min = e[["id" , "percentage" , "attendence_percentage"]].min()
print("min is",min)

max = e[["id" , "percentage" , "attendence_percentage"]].max()
print("max is",max)

quantile1 = e[["id" , "percentage" , "attendence_percentage"]].quantile(0.25)
print("25 qualntile  is",quantile1)

quantile2 = e[["id" , "percentage" , "attendence_percentage"]].quantile(0.50)
print("50 qualntile  is",quantile2)

#outliers by using IQR 
def outliers(data , column):
 IQR = quantile2-quantile1
 print(IQR)

 upper_bound = quantile1 - 1.5 * IQR
 lower_bound = quantile2 + 1.5 * IQR

 outliers = e[(e[column] < lower_bound) |(e["column"] > upper_bound)]
 print(list(outliers))
#corelattion


x = e["percentage"]
y = e["attendence_percentage"]

num = np.sum((x - x.mean()) * (y -y.mean()))
denum = np.sqrt(np.sum(x - x.mean()** 2) * (np.sum(y -y.mean()** 2)))
cor = num / denum
print("corr is" , cor)

#regression line
m = num/(np.sum(x - x.mean()** 2))
c = (y.mean() - m * (x.mean()))
print("c=", c)

#bar graph
x = e["attendence_percentage"]
y = e["percentage"]

plt.bar(x , y)
plt.show()


x = e["id"]
y = e["name"]

plt.bar(x , y)
plt.show()

#pie graph
x = e["attendence_percentage"]
y = e["percentage"]

plt.pie(y)
plt.show()


x = e["id"]
y = e["name"]

plt.pie(x)
plt.show()

x = e["attendence_percentage"]
y = e["percentage"]

plt.hist(x,y=10)
plt.bar(x,y)
plt.xlabel("attendence_percentage")
plt.ylabel("percentage")
plt.show()

x = e["id"]
y = e["name"]

plt.grid(True)
plt.bar(x,y)
plt.xlabel("id")
plt.ylabel("name")
plt.show()

x = e["attendence_percentage"]
y = e["percentage"]
plt.legend(x,y)
plt.bar(x,y)
plt.show()















