import sqlite3
  
con = sqlite3.connect("bcb.h2.db")
con.execute("select * from FUNCTIONALITIES ")
