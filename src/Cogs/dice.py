import discord
from discord.ext import commands
from discord import app_commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='주사위', description='주사위를 굴립니다.')
    async def dice(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        num = random.randrange(1, 7)
        await interaction.followup.send(f'{num}')

async def setup(bot):
    await bot.add_cog(Dice(bot))