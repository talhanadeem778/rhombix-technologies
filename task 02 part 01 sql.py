import sqlite3
import csv


conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    customer_id INTEGER,
    gender TEXT,
    region TEXT,
    age INTEGER,
    product_name TEXT,
    category TEXT,
    unit_price REAL,
    quantity INTEGER,
    total_price REAL,
    shipping_fee REAL
)
""")

cursor.execute("INSERT INTO sales VALUES (1,'Male','Islamabad',45,'Laptop','Tech',14000,4,56000,2000)")
cursor.execute("INSERT INTO sales VALUES (2,'Female','Lahore',30,'Mobile','Tech',50000,1,50000,500)")
cursor.execute("INSERT INTO sales VALUES (3,'Male','Karachi',35,'Headphones','Tech',3000,2,6000,300)")
cursor.execute("INSERT INTO sales VALUES (4,'Female','Faisalabad',28,'Shoes','Fashion',4000,2,8000,250)")
cursor.execute("INSERT INTO sales VALUES (5,'Male','Multan',40,'Watch','Accessories',7000,1,7000,200)")
cursor.execute("INSERT INTO sales VALUES (6,'Female','Peshawar',26,'Bag','Fashion',2500,3,7500,150)")
cursor.execute("INSERT INTO sales VALUES (7,'Male','Rawalpindi',32,'Keyboard','Tech',3500,2,7000,180)")
cursor.execute("INSERT INTO sales VALUES (8,'Female','Sialkot',29,'Mouse','Tech',1200,4,4800,100)")
cursor.execute("INSERT INTO sales VALUES (9,'Male','Quetta',37,'Printer','Tech',18000,1,18000,600)")
cursor.execute("INSERT INTO sales VALUES (10,'Female','Hyderabad',24,'Dress','Fashion',5000,2,10000,250)")
cursor.execute("INSERT INTO sales VALUES (11,'Male','Gujranwala',33,'Tablet','Tech',30000,1,30000,700)")
cursor.execute("INSERT INTO sales VALUES (12,'Female','Bahawalpur',27,'Book','Education',800,5,4000,100)")
cursor.execute("INSERT INTO sales VALUES (13,'Male','Sargodha',31,'Camera','Electronics',45000,1,45000,900)")
cursor.execute("INSERT INTO sales VALUES (14,'Female','Abbottabad',36,'Jacket','Fashion',6500,2,13000,300)")
cursor.execute("INSERT INTO sales VALUES (15,'Male','Mardan',42,'Speaker','Electronics',8500,2,17000,400)")
cursor.execute("INSERT INTO sales VALUES (16,'Female','Kasur',23,'Perfume','Beauty',3000,3,9000,150)")
cursor.execute("INSERT INTO sales VALUES (17,'Male','Okara',39,'Monitor','Tech',22000,1,22000,500)")
cursor.execute("INSERT INTO sales VALUES (18,'Female','Sheikhupura',34,'Handbag','Fashion',5500,2,11000,250)")
cursor.execute("INSERT INTO sales VALUES (19,'Male','Rahim Yar Khan',41,'Router','Tech',6000,2,12000,300)")
cursor.execute("INSERT INTO sales VALUES (20,'Female','Sahiwal',25,'Power Bank','Electronics',2500,3,7500,200)")
conn.commit()

rows = cursor.fetchall()
for row in rows:
 print(row)      


cursor.execute("select * from sales where category = 'Tech'")
rows = cursor.fetchall()
for row in rows:
 print(row)

cursor.execute("select * from sales where product_name  = 'Handbag'")
rows = cursor.fetchall()
for row in rows:
 print(row )

#and 
cursor.execute("""
select * from sales where gender = 'Male' AND  product_name = 'Laptop'
""")
rows = cursor.fetchall()
for row in rows:
 print(row)

#or
cursor.execute("""
select * from sales where gender = 'Female' OR  product_name = 'Dress'
""")
rows = cursor.fetchall()
for row in rows:
 print(row)

#sum
cursor.execute("""
select sum(total_price) from sales
""") 
rows = cursor.fetchall()
for row in rows:
 print(row)

#avg
cursor.execute("""
select avg(total_price) from sales
""") 
rows = cursor.fetchall()
for row in rows:
 print(row)

#max
cursor.execute("""
select max(unit_price) from sales
""") 
rows = cursor.fetchall()
for row in rows:
 print(row)

#min
cursor.execute("""
select min(unit_price) from sales
""") 
rows = cursor.fetchall()
for row in rows:
 print(row)

conn = sqlite3.connect("e_commerce.db")
data =  cursor.execute("""
CREATE TABLE IF NOT EXISTS e_commerce (
customer_id INT PRIMARY KEY,
product_name VARCHAR(50),
quantity REAL,
unit_price real,
total_price real
)
""")
cursor.execute("INSERT INTO  e_commerce VALUES (1, 'Laptop', 2, 50000, 100000)")
cursor.execute("INSERT INTO  e_commerce VALUES (2, 'Mobile', 1, 35000, 35000)")
cursor.execute("INSERT INTO  e_commerce VALUES (3, 'Headphones', 3, 2500, 7500)")
cursor.execute("INSERT INTO  e_commerce VALUES (4, 'Keyboard', 2, 1800, 3600)")
cursor.execute("INSERT INTO  e_commerce  VALUES (5, 'Mouse', 4, 900, 3600)")
cursor.execute("INSERT INTO  e_commerce VALUES (6, 'Tablet', 1, 28000, 28000)")
cursor.execute("INSERT INTO  e_commerce VALUES (7, 'Smart Watch', 2, 12000, 24000)")
cursor.execute("INSERT INTO  e_commerce VALUES (8, 'Speaker', 3, 3500, 10500)")
cursor.execute("INSERT INTO  e_commerce VALUES (9, 'Power Bank', 5, 2000, 10000)")
cursor.execute("INSERT INTO  e_commerce VALUES (10, 'USB Cable', 10, 500, 5000)")
cursor.execute("INSERT INTO  e_commerce  VALUES (11, 'Printer', 1, 18000, 18000)")
cursor.execute("INSERT INTO  e_commerce VALUES (12, 'Monitor', 2, 22000, 44000)")
cursor.execute("INSERT INTO  e_commerce VALUES (13, 'Camera', 1, 65000, 65000)")
cursor.execute("INSERT INTO  e_commerce VALUES (14, 'SSD', 3, 8000, 24000)")
cursor.execute("INSERT INTO  e_commerce VALUES (15, 'Hard Drive', 2, 7000, 14000)")
cursor.execute("INSERT INTO  e_commerce VALUES (16, 'Router', 4, 4500, 18000)")
cursor.execute("INSERT INTO  e_commerce VALUES (17, 'Webcam', 3, 6000, 18000)")
cursor.execute("INSERT INTO  e_commerce VALUES (18, 'Microphone', 2, 7500, 15000)")
cursor.execute("INSERT INTO  e_commerce VALUES (19, 'Gaming Chair', 1, 30000, 30000)")
cursor.execute("INSERT INTO  e_commerce VALUES (20, 'Graphics Card', 1, 95000, 95000)")
conn.commit()

cursor.execute("select * from e_commerce limit 20")
rows = cursor.fetchall()
for row in rows:
 print(rows)
#where
cursor.execute("select * from e_commerce where unit_price = 18000")
rows = cursor.fetchall()
for row in rows:
 print(rows) 

#order by 
cursor.execute("select * from e_commerce ORDER BY product_name , quantity ASC")
rows = cursor.fetchall()
for row in rows:
 print(rows)

#group by
cursor.execute("select product_name,sum(total_price) from e_commerce GROUP BY total_price ")
rows = cursor.fetchall()
for row in rows:
 print(rows)

#joins 
cursor.execute("""
select sales.customer_id ,
   sales.gender ,
   sales.quantity ,
   e_commerce.customer_id ,
   e_commerce.product_name ,
   e_commerce.quantity
FROM sales
INNER JOIN  e_commerce
ON sales.customer_id  = e_commerce.customer_id 
""")
print("inner join")

rows = cursor.fetchall()
for row in rows:
 print(row)

cursor.execute("""
select sales.category ,
       sales.unit_price ,
       e_commerce.quantity , 
       e_commerce.unit_price
FROM sales
left join e_commerce
ON sales.unit_price = e_commerce.unit_price
""")
print("left join") 
rows = cursor.fetchall()
for row in rows:
 print(row)

cursor.execute("""
select sales.category ,
       sales.unit_price ,
       e_commerce.quantity , 
       e_commerce.unit_price
FROM sales
right join e_commerce
ON sales.unit_price = e_commerce.unit_price
""") 
print("right join")

rows = cursor.fetchall()
for row in rows:
 print(row) 


cursor.execute("""
select sales.total_price , 
       sales.shipping_fee , 
       e_commerce.total_price , 
       e_commerce.product_name
from sales
outer full join e_commerce
on  sales.total_price = e_commerce.total_price       
""")
rows = cursor.fetchall()
for row in rows:
 print(row)

conn.commit()
conn.close()







