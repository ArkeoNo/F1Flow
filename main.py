from http import client
import discord
from discord.ext import commands
import fastf1 as ff1
import json

config = json.load(open('config.json'))
bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
    print(f'{bot.user} Connecté à Discord')

bot.run(config['token'])