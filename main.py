import discord
from discord.ext import commands
import fastf1 as ff1
import json
from commandes.bet import fbet

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
    await ctx.send('paris sauvgardé')

bot.run(config['token'])