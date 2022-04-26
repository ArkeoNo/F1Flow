import commandes.db as db

np_pilote = ['1', '3', '4', '5', '6', '10','11', '14', '16', '18', '20', '22', '23', '24', '31', '33', '44', '47', '55', '63', '77']

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
            pod = [args[1], args[2], args[3]]
            podium = '-'.join([str(item) for item in pod ])
            if pod[0] in np_pilote and pod[1] in np_pilote and pod[2] in np_pilote : 
                bet = [ctx.author.id, somme, podium] 
                print(bet)
                await db.add(bet)
                await ctx.send('paris sauvgardé')
            else : 
                await ctx.send('Erreur de Syntaxe  - code : B03 .. \n l\'un des ID Pilote est incorect, pour rappel il faut utiliser les numéros permanant des pilotes')
        else : 
            await ctx.send('Erreur de Syntaxe 2 - code : B02 ..\n Besoin d\' aide ? => //help')
    else :
        await ctx.send('Erreur de Syntaxe - code : B01 ..\n Besoin d\' aide ? => //help')
