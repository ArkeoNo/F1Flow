from discord.ext import commands
import fastf1 as ff1
import json
from commandes.bet import fbet
import commandes.results as reslt
import commandes.db as data

config = json.load(open('config.json'))
bot = commands.Bot(command_prefix=config['prefix'])
ff1.Cache.enable_cache('./data/cache')

#Pour les tests, le GP utilisé est celui de Bahrein de l'année dernière
session = ff1.get_session(2022, 2)
print(f'Session chargée : {session.name}')

@bot.event
async def on_ready():
    print(f'{bot.user} Connecté à Discord')

@bot.command()
async def bet(ctx, *args):
    await fbet(ctx, args)
    print(f'Nouveau paris de {ctx.author}')

@bot.command()
async def res(ctx):
    await reslt.bet()

@bot.command()
async def Del_Bets(ctx):
    await data.del_bets()

@bot.command()
async def Del_Users(ctx):
    await data.del_users()


bot.run(config['token'])
