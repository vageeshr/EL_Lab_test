import mysql.connector
import sys
import datetime
global conn,cursor;

conn = mysql.connector.connect(host="localhost",user="root")

def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def create_database():
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE db_181041006")
            print("\n Successfully database created \n" )
        except:
            print("Warning: Database already exists \n")
    else:
        print("\nCould not connect to mysql server \n")
 
def create_table():
	conn_db=mysql.connector.connect(host="localhost",db="db_181041006",user="root")
	if conn_db.is_connected():
		cursor=conn_db.cursor()
		try:
			cursor.execute("CREATE TABLE reg_no(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
			print("Successfully created tABLE")
		except:
			print("Warning:already created")
	else:
		print("fail connection")
		conn_db.close()


def insert_values():
	db_conn=mysql.connector.connect(host="localhost",db="db_181041006",user="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		query = "INSERT INTO reg_no(id, fname, lname,dob) VALUES (%s,%s,%s,%s) "
		id = input("\n Enter id\n")
		fname = input("\n Enter first name\n")
		lname = input("\n Enter last name\n")
		dob=input("\n Enter date of birth (yyyy/mm/dd)\n")
		value=(id,fname,lname,dob)
		mycursor.execute(query,value)
		db_conn.commit()
		print("sucessfully inserted")

		if not validate(dob):
			print("Incorrect format.Enter in yyyy/mm/dd format ")
			sys.exit()

	db_conn.close()


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
    	return False
	
def display():
	conn_db=mysql.connector.connect(host="localhost",db="db_181041006",user="root")
	if conn_db.is_connected():
		cursor=conn_db.cursor()
		try:
			cursor.execute("SELECT * FROM reg_no")
			rows = cursor.fetchall();
			for row in rows:
   				print(row);
		except:
			print("Warning:already created")
	else:
		print("fail connection")
		conn_db.close()
def alter_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041006", user="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        col = input("\nEnter column name\n")
        sql = "ALTER TABLE reg_no add %s VARCHAR(255)" % (col)

        try:
            mycursor.execute(sql)
            conn_db.commit()
            print("Column created\n")
        except:
         	print("column already exist\n")
    else:
    	print("connection failed\n")

def truncate():
	conn_db=mysql.connector.connect(host="localhost",db="db_181041006",user="root")
	if conn_db.is_connected():
		mycursor=conn_db.cursor()
		sql="DROP TABLE reg_no"
		try:
			mycursor.execute(sql)
			conn_db.commit()
			print("table deleted\n")
		except:
			print("Cannot deleted\n")
	else:
		print("connection failed\n")
	conn_db.close()
def main():
	connection();
	while True:
		print("\nEnter your choice::\n")
		print( "Create database - 1:" )
		print( "Create table (reg_no) - 2:")
		print( "Insert values (reg_no) - 3:")
		print("Display table values (reg_no) - 4:")
		print("Alter table (add column) - 5:")
		print("Trucate table (reg_no) - 6:")
		print("Quit- q:\n")
		choice = input("Enter the option:\t")
		
		
		if choice == '1':
			create_database()
		if choice == '2':
			create_table()
		if choice == '3':
			insert_values()
		if choice == '4':
			display()
		if choice == '5':
			alter_table()
		if choice == '6':
			truncate()
		if choice == 'q':
			sys.exit()
		


if __name__ == "__main__":
	main();
	
