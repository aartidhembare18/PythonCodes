#!/user/bin/python3
import sqlite3
conn=sqlite3.connect("test1.db")
c=conn.cursor()
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS table1(name TEXT,rno REAL)")
def put_static_data():
	c.execute("INSERT INTO table1 VALUES('xyz',9)")
	conn.commit()
	
	
def put_dynamic_data():
	for i in range(3):
		name1=input("enter a name")
		rno1=int(input("enter a roll no"))
		c.execute("INSERT INTO table1(name,rno)VALUES(?,?)",(name1,rno1))
		conn.commit()
	
	
def display_data():
	c.execute("SELECT *FROM table1")
	d=c.fetchall()
	print(d)
def update_data():
	name1=input("enter name which has to be change")
	change_name=input("enter new name")
	c.execute("UPDATE table1 SET name=? WHERE name=?",(change_name,name1))
	conn.commit()
	
	
def delete_data():
	rno1=int(input("enter a roll no to remove a data"))
	c.execute("DELETE FROM table1 WHERE rno=%d"%(rno1))
	conn.commit()

	
create_table()
put_static_data()
put_dynamic_data()
display_data()
update_data()
delete_data()
display_data()
                     
