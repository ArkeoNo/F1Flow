import discord
import json

np_pilote = ['1', '3', '4', '5', '6', '10','11', '14', '16', '18', '20', '22', '23', '24', '31', '44', '47', '55', '63', '77']

def tryint(string) :
    try : 
        int(string)
        return True
    except ValueError:
        return False


async def fbet(ctx, args):
    if len(args) == 4 :
        somme = args[0]
        if tryint(somme) :
            somme = int(somme)
            p1 = args[1]
            p2 = args[2]
            p3 = args[3]
            if p1 in np_pilote and p2 in np_pilote and p3 in np_pilote :
                await ctx.send('Good')
                bet =  {"id" : ctx.author.id, "amount" : somme, "podium" : [p1, p2, p3]}
                return bet
            else : 
                await ctx.send('Erreur de Syntaxe  - code : B03 .. \n l\'un des ID Pilote est faux, pour rappel il faut utiliser les numéros permanant des pilotes')
        else : 
            await ctx.send('Erreur de Syntaxe 2 - code : B02 ..\n Besoin d\' aide ? => //help')
    else :
        await ctx.send('Erreur de Syntaxe - code : B01 ..\n Besoin d\' aide ? => //help')
