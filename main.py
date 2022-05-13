from discord.ext import commands
import fastf1 as ff1
import json
from commandes.bet import fbet
import commandes.results as reslt
import commandes.db as data
import commandes.stats as stats

config = json.load(open('config.json'))
bot = commands.Bot(command_prefix=config['prefix'])
ff1.Cache.enable_cache('./data/cache')

#Pour les tests, le GP utilisé est celui de Bahrein de l'année dernière
session = ff1.get_session(2022, 2)
print(f'Session chargée : {session.name}')

@bot.event
async def on_ready():
    print(f'{bot.user} Connecté à Discord')

@bot.command() # Créé une nouvelle entrée dans la base de donné
async def bet(ctx, *args):
    await fbet(ctx, args)
    print(f'Nouveau paris de {ctx.author}')

@bot.command() # Génére les resultats et modifie les montant utilisateur sur la DB
async def res(ctx):
    await reslt.bet()

@bot.command() # Vide la table de paris
async def Del_Bets(ctx):
    await data.del_bets()

@bot.command() # Vide la Table des Utilisateurs
async def Del_Users(ctx):
    await data.del_users()

@bot.command()
async def profile(ctx) :
    await stats.profile(ctx)



bot.run(config['token'])

