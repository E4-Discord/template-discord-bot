import discord
from discord.ext import commands
from discord import app_commands
import random

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @app_commands.command(name='테스트', description='테스트 전용 명령어입니다.')
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'테스트 성공!')

async def setup(bot):
    await bot.add_cog(Test(bot))