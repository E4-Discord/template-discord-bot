import discord
from discord.ext import commands

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='안녕')
    async def hello(self, ctx):
        await ctx.channel.send('안녕하세요!')

async def setup(bot):
    await bot.add_cog(HelloWorld(bot))