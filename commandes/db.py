import sqlite3

conn = sqlite3.connect('./data/Ubet.db') 
c = conn.cursor()

async def add(bet) : #  Fonction pour ajouter un paris à la DB
    lignes = []
    d = c.execute(f"SELECT * FROM bets WHERE id = {bet[0]}")
    for ligne in d :
        lignes.append(ligne)
    if len(lignes) > 0 :
        c.execute(f"UPDATE bets SET ammount = {bet[1]}, podium = '{bet[2]}'")
    else :
        c.execute("INSERT INTO bets VALUES (?,?,?)", bet)
    conn.commit()

async def read_bets() : #Fonction pour récuper les paris sauvgardé
    bets = []    
    p = c.execute("SELECT * FROM bets")
    for bet in p :
        bets.append(bet)
    return bets

async def READ_User_data(user) :
    lignes = []
    d = c.execute(f"SELECT * FROM users WHERE id = {user}")
    for ligne in d :
        lignes.append(ligne)
    u = ligne
    return u

async def UPDATE_User_Ammount(user): # Fonction pour Mettre à jour les points d'un Joueur
    lignes = []
    d = c.execute(f"SELECT * FROM users WHERE id = {user[0]} ")
    for ligne in d :
        lignes.append(ligne)
    pts = lignes[0][1] + user[1]
    if len(lignes) > 0 :
        c.execute(f"UPDATE users SET ammount = {pts} WHERE id = {user[0]}")
    else :
        u = (user[0], user[1])
        c.execute("INSERT INTO users VALUES (?,?)", u)
    conn.commit()

async def close(save): # Ferme la connection avec la DB
    if save :
        conn.commit()
    conn.close()

async def del_bets(): # VIDE la table de PARIS
    c.execute("DELETE FROM bets")
    conn.commit()
    print('Table des paris vidée')

async def del_users(): # VIDE la table des UTILISATEUR
    c.execute("DELETE FROM users")
    conn.commit()
    print('Table des utilisateur vidée')
