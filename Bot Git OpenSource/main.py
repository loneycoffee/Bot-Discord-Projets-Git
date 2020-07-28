import discord
import os
from discord.ext import commands
import asyncio


print('Chargement...')

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

# Configuration

token = '' #token du bot
emoji_erreur ="" #emoji erreur

# Lancement du bot

@bot.event
async def on_ready():
    print('Bot lancé')
    await bot.change_presence(status = discord.Status.online)
    while not bot.is_closed():
        await bot.change_presence(activity=discord.Streaming(name=f"!git en mp 📌", url="https://www.twitch.tv/gravenyt"))
        await asyncio.sleep(30)
        await bot.change_presence(activity=discord.Streaming(name=f"Vendre TableBasse 💲",url="https://www.twitch.tv/dr_tablebasse"))
        await asyncio.sleep(7)
        await bot.change_presence(activity=discord.Streaming(name=f"Lokdien le Bg 🍷", url="https://www.twitch.tv/lokdien"))
        await asyncio.sleep(7)
        await bot.change_presence(activity=discord.Streaming(name=f"Loney ak ☕", url="https://www.twitch.tv/loneycoffee"))
        await asyncio.sleep(7)
        await bot.change_presence(activity=discord.Streaming(name=f"Baptou le King 👑", url="https://www.twitch.tv/gravenyt"))
        await asyncio.sleep(7)


# Error handler

@bot.event
async def on_command_error(ctx,error):
	pass

@bot.event
async def on_message(message):
	await asyncio.sleep(0)
	await bot.process_commands(message)


# Chargement des Cogs

for fichier in os.listdir(f'./cmds'):
    if fichier.endswith('.py'):
        bot.load_extension(f'cmds.{fichier[:-3]}')


bot.run(token)
