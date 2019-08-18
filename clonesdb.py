import sqlite3

con = sqlite3.connect("clones.db")
con.execute("create table clone_data (uid INTEGER PRIMARY KEY AUTOINCREMENT, Clone1 TEXT NOT NULL, Clone2 TEXT NOT NULL, BCB_RATING INTEGER NOT NULL, P1 INTEGER NOT NULL, P2 INTEGER NOT NULL)")
con.close()

