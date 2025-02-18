import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
DB_USERNAME = os.environ.get("DB_USERNAME","1234")
DB_PASSWORD = os.environ.get("DB_PASSWORD","1234")

mydb = mysql.connector.connect(
  host="localhost",
  user=DB_USERNAME,
  password=DB_PASSWORD
)
cursor=mydb.cursor()
cursor.execute("use website")
from .user import UserData
from .message import MessageData