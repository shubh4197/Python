import csv
import pymysql

db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
cursor.execute("""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         CITY CHAR(20))""")
# resp=cursor.fetchall()
# print(resp)
# for row in resp:
#	print(row["fname"] , row["lname"])
# db.commit()

reader = csv.reader(open('demo.csv', 'r'), delimiter=',')
for data in reader:
    cursor.execute("""INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME,CITY)
            VALUES ('{0}','{1}','{2}')""".format(*data)
                   )
db.commit()
db.close()
