import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # 멤버 목록 접근 허용
intents.message_content = True   # 메시지 내용 읽기 허용

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def 유저목록(ctx):
    members = ctx.guild.members
    member_names = []

    for member in members:
        nickname = member.display_name  # 닉네임 가져오기
        parts = nickname.split("/")
        if len(parts) > 1:
            first = parts[0]
            splittedfirst = first.split(" ")
            # 세 번째 단어가 존재하는지 확인
            if len(splittedfirst) >= 3:
                member_names.append(splittedfirst[2])
        else:
            member_names.append("#" + nickname)

    output = "\n".join(member_names)
    await ctx.send(f"서버 유저 목록:\n{output}")

bot.run(os.environ['TOKEN'])