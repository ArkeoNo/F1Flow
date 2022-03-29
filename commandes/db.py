import sqlite3

conn = sqlite3.connect('./data/Ubet.db') 
c = conn.cursor()

c.execute("""CREATE TABLE bets (
 id integer,
 ammount integer,
 podium text
)""")

c.execute("""CREATE TABLE users (
 id integer,
 ammount integer
)""")

async def add(bet) : #  Fonction pour ajouter un paris à la DB
    conn = sqlite3.connect('./data/Ubet.db') 
    c = conn.cursor()
    c.execute("INSERT INTO bets VALUES (?,?,?)", bet)
    conn.commit()
    conn.close()

async def read() : #Fonction
    conn = sqlite3.connect('./data/Ubet.db') 
    c = conn.cursor()
    c.execute("SELECT")
