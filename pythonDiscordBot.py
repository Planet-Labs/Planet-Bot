import discord
from discord.ext import commands
#discord와의 연결에 필요한 파일을 불러옵니다.

client = commands.Bot(command_prefix = '~')
#discord에서 사용할 명령어 접두사를 말합니다. ex) ~help

token = "671672698547601418"
#input your Token을 지우고 여러분의 토큰을 넣어주세요.

client.run(token)
#discord봇을 실행시키는 함수입니다.