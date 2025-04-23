import discord
from discord.ext import commands
from dico_token import Token
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# 명령어 추가
async def load_extensions():
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    await load_extensions()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('개발'))

# 봇 실행

bot.run(Token)