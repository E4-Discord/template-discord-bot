import discord
from discord.ext import commands

class ByeWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='잘가')
    async def bye(self, ctx):
        await ctx.channel.send('안녕히 가세요!')

async def setup(bot):
    await bot.add_cog(ByeWorld(bot))