import discord
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, application_id=os.getenv('BOT_ID'))

@bot.event
async def on_ready():
    print(f'{bot.user} Está online e pronto para uso.')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizado {len(synced)} comando(s)!")
    except Exception as erro:
        print(f"Erro ao sincronizar comandos: {erro}")     

async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')

async def main():
    await load()
    await bot.start(os.getenv('BOT_SECRET'))

asyncio.run(main())
