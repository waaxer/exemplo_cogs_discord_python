import discord
from discord.ext import commands
import config

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cog = __class__.__name__

    def cog_load(self):
        print(f"Evento: {self.cog} foi carregado!")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)
        
async def setup(bot):
    await bot.add_cog(OnMessage(bot))
