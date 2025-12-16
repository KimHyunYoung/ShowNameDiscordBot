import discord
from discord.ext import commands
import os
import re


intents = discord.Intents.default()
intents.members = True  # 멤버 목록 접근 허용
intents.message_content = True   # 메시지 내용 읽기 허용
intents.voice_states = True   # 음성 상태 접근 허용

def remove_non_alnum(text):
    # 영어 대소문자(A-Z, a-z)와 숫자(0-9)만 남기고 나머지는 모두 제거
    return re.sub(r'[^A-Za-z0-9]', '', text)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def 참여자(ctx):
    output = []

    for vc in ctx.guild.voice_channels:
        allowed_names = ["ookami812", "minseokkoo"]
        if ctx.author.name not in allowed_names:
            return

        if vc.members: 
            member_names = []
            for members in vc.members:
                nickname = members.display_name  # 닉네임 가져오기
                nickname = remove_non_alnum(nickname)  # 이모지 제거
                parts = nickname.split("/")
                if len(parts) > 1:
                    first = parts[0]
                    splittedfirst = first.split(" ")
                    if len(splittedfirst) >= 3:
                        member_names.append(splittedfirst[-1])
            output.append(f"{vc.name}\n" + "\n".join(member_names))

    await ctx.send("\n\n".join(output))

bot.run(os.environ['TOKEN'])