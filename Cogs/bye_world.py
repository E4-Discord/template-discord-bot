import discord
from discord.ext import commands
from discord import app_commands

class ByeWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='잘가', description='봇에게 작별 인사를 합니다.')
    async def bye(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'안녕히 가세요, {interaction.user.display_name}님!')

async def setup(bot):
    await bot.add_cog(ByeWorld(bot))