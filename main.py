import discord
import asyncio
from discord.ext import commands
import os
import pathlib
import sys
from dotenv import load_dotenv

sys.dont_write_bytecode = True
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
    path = pathlib.Path("./commands")
    for file in path.glob("**/*.py"):
        if file.is_file():
            extension = ".".join(file.parts)[:-3]
            await bot.load_extension(extension.replace("/", "."))

    path = pathlib.Path("./events")
    for file in path.glob("**/*.py"):
        if file.is_file():
            extension = ".".join(file.parts)[:-3]
            await bot.load_extension(extension.replace("/", "."))

async def main():
    await load()
    await bot.start(os.getenv('BOT_SECRET'))

asyncio.run(main())
