import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # 멤버 목록 접근 허용
intents.message_content = True   # 메시지 내용 읽기 허용
intents.voice_states = True   # 음성 상태 접근 허용

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def 음성유저(ctx):
    output = []

    for vc in ctx.guild.voice_channels:
        allowed_names = ["오오카미"]
        output.append(f">사용자: {ctx.author.name}\n")
        if ctx.author.name not in allowed_names:
            return

        if vc.members: 
            member_names = []
            for members in vc.members:
                nickname = members.display_name  # 닉네임 가져오기
                parts = nickname.split("/")
                if len(parts) > 1:
                    first = parts[0]
                    splittedfirst = first.split(" ")
                    if len(splittedfirst) >= 3:
                        member_names.append(splittedfirst[-1])
            output.append(f">{vc.name} 채널:\n" + "\n".join(member_names))

    await ctx.send("\n\n".join(output))

bot.run(os.environ['TOKEN'])