
import fastf1 as ff1
import commandes.db as data

gp_num = 2

def racer() :    
    reslist=[]
    race = ff1.get_session(2022, gp_num).get_race()
    result = race.results
    for driver in result :
        reslist.append(driver['Driver']['permanentNumber'])
    print(f' Résultats de la Course : {reslist}')
    return reslist

async def bet():
    race = racer()
    db = await data.read()
    for bet in db :
        coef = 1
        discID = bet[0]
        podium = bet[2].split('-')  
        if race[0] == podium[0]:
            coef += 0.75
        if race[1] == podium[1]:
            coef += 0.5
        if race[2] == podium[2]:
            coef += 0.25
        if race[0] == podium[0] and race[1] == podium[1] and race[2] == podium[2] :
            coef = 3
        if coef == 1 :
            coef = 0
        pts =(bet[1]*coef)-bet[1]
        u = (discID, pts, bet[1])
        print(f'{discID} à Gagné/Perdu {pts} points || {u} || Coef: {coef}')
        await data.UPDATE_User_Ammount(u)

