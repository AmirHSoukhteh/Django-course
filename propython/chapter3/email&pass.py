from mysql.connector import connect, Error
from getpass import getpass
import re

db_user = input("Enter you'r user database's name: ")
db_password = getpass("Enter your database's password: ")

#Create database
try:
  mydb = connect(
  host = "localhost",
  user = db_user,
  password = db_password,
  )

  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE Email")
except:
  print("DATABASE WAS ALREADY EXISTSED.")

#Create Table

try:
    mydb = connect(
    host = "localhost",
    user = db_user,
    password = db_password,
    database = "Email"
    )
    mycursor.execute("CREATE TABLE information (username VARCHAR(255), password VARCHAR(255))")
except:
  print("Table was already existed")

def check():
  email = input("Enter your email addres: ")
  pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
  if re.match(pat,email):
      return email
  else:
      print("Invalid Email , ", "(expression@string.string)")
      check()

def collect_email():

  username = check()
  password = input("Enter your email's password: ")
  
  mydb = connect(
  host = "localhost",
  user = db_user,
  password = db_password,
  database = "Email"
  )
  
  mycursor = mydb.cursor()
  sql = "INSERT INTO information (username, password) VALUES (%s, %s)"
  val = (username, password)
  mycursor.execute(sql, val)
  mydb.commit()

collect_email()