import discord
from discord.ext import commands
from discord import app_commands

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='안녕', description='봇에게 인사를 건넵니다.')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'안녕하세요, {interaction.user.display_name}님!')

async def setup(bot):
    await bot.add_cog(HelloWorld(bot))