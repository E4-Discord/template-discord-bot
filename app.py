import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class Bot(commands.Bot):
    def __init__(self):
        # 봇 권한 설정
        # Discord 개발자 포털 > 봇 > Message Content Intent 활성화 필수
        intents = discord.Intents.default()
        intents.message_content = True
        
        # @app_commands.command는 슬래시(/) 명령어로 호출 가능
        # @commands.hybrid_command는 슬래시(/)와 접두사(!) 명령어 둘 다 사용 가능
        super().__init__(command_prefix='!', intents=intents)

        # 환경 변수 로드
        load_dotenv()

        # 디스코드 봇 토큰 가져오기
        self.token = self.get_token('discord_bot_token')

    async def setup_hook(self):
        # Cogs 폴더 안의 명령어 로드
        for filename in os.listdir('Cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'Cogs.{filename[:-3]}')
        
        # 디스코드 서버에 슬래시(/) 명령어 동기화
        await self.tree.sync()
        print('명령어 동기화 완료!')

    async def on_ready(self):
        print(f'로그인 됨: {self.user}')
        
        # 봇의 상태창 설정 ("~하는 중" 표시)
        await self.change_presence(status=discord.Status.online, activity=discord.Game('테스트 중'))

    def get_token(self, secret_name):
        secret_path = f'/run/secrets/{secret_name}'
        try:
            with open(secret_path, 'r', encoding='utf-8') as f:
                print(f'Docker secret을 사용합니다: {secret_name}')
                return f.read().strip()
        except FileNotFoundError:
            print(f'환경 변수를 사용합니다: {secret_name}')
            return os.getenv(secret_name)

if __name__ == "__main__":
    bot = Bot()
    bot.run(bot.token)