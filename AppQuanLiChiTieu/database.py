import sqlite3
conn=sqlite3.connect("Manage.db")
print("opened database successfully!")
try:
    conn.execute("""CREATE TABLE IF NOT EXISTS Expense
    (username CHAR(10)  NOT NULL,
    item CHAR(20) NOT NULL,
    tag TEXT NOT NULL,
    type TEXT NOT NULL,
    amount INT ,
    edate CHAR(10)
    );""")
except:
    print()

print("Table created successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS User
    (
    username CHAR(20) NOT NULL,
    contact CHAR(20) NOT NULL,
    email CHAR(20) NOT NULL,
    security CHAR(20) NOT NULL,
    password CHAR(20) NOT NULL 
    );''')
print("Table created successfully")

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Budget
    (
    username CHAR(20) NOT NULL,
    item CHAR(20) NOT NULL,
    lim INT
    );''')

except:
    print()
li=[['Tuan','pizza','others','expense',200,'2022/11/03'],
['Tuan','movie','entertainment','expense',300,'2022/11/22'],
['Tuan','salary','pension','income',1000,'2022/11/25'],
['Tuan','bill','utilities','expense',500,'2022/10/02'],
['Tuan','diwali','gift income','income',500,'2022/10/02'],
['Tuan','salary','salary','income',10000,'2022/09/01'],
['Tuan','child edu','Education','expense',5000,'2022/09/01'],
['Tuan','bonus','bonus','income',2000,'2022/08/28'],
['Tuan','other','others','expense',1000,'2022/08/28']]
print("Table created successfully")
for i in li:
    conn.execute("""INSERT INTO Expense VALUES(?,?,?,?,?,?);""",i)
print("data entry successful!")
conn.commit()
print("now showing the data: ")

conn.execute("""INSERT INTO User VALUES('Tuan','0337383962','tuan@gmail.com','123456','123456')""")
conn.commit()

conn.execute("INSERT INTO Budget VALUES('Tuan','movie',1000)")
conn.commit()