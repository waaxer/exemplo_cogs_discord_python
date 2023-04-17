import discord
from discord import app_commands
from discord.ext import commands

class nome_classe_comando(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Comando carregado.')

    @app_commands.command(name="teste", description="teste")
    @app_commands.describe()
    async def nome_comando(self, interaction: discord.Interaction):
        print("exemplo")

async def setup(bot):
    await bot.add_cog(nome_classe_comando(bot))