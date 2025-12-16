import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # 멤버 목록 접근 허용

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def 유저목록(ctx):
    members = ctx.guild.members
    member_names = [member.name for member in members]
    # 너무 길어질 수 있으니 20명까지만 출력
    output = "\n".join(member_names[:20])
    await ctx.send(f"서버 유저 목록 (일부):\n{output}")

bot.run(os.environ['TOKEN'])