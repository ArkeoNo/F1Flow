from turtle import color
from matplotlib.pyplot import title
import commandes.db as db
import discord

async def profile(ctx) : 
    
    user_id = ctx.author.id
    user_data = await db.READ_User_data(user_id)
    ammount = user_data[1]

    embed = discord.Embed(color = discord.Color.dark_magenta())
    embed.set_author(name=f"Profil de {ctx.author.display_name}", icon_url= ctx.author.avatar_url)
    embed.add_field(name="Porte-Feuille :", value=f"{ammount} $")
    
    await ctx.send(embed=embed)