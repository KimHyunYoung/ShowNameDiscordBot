import discord
from discord.ext import commands
import os
import re

intents = discord.Intents.default()
intents.members = True  # 멤버 목록 접근 허용
intents.message_content = True   # 메시지 내용 읽기 허용
intents.voice_states = True   # 음성 상태 접근 허용


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # 😀 ~ 😏 (이모티콘)
        "\U0001F300-\U0001F5FF"  # 🌍 ~ 🗿 (기호 & 그림)
        "\U0001F680-\U0001F6FF"  # 🚀 ~ 🚻 (교통 & 지도)
        "\U0001F1E0-\U0001F1FF"  # 🇰🇷 ~ 🇺🇸 (국기)
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.command()
async def 음성유저(ctx):
    output = []

    for vc in ctx.guild.voice_channels:
        allowed_names = ["ookami812", "minseokkoo"]
        if ctx.author.name not in allowed_names:
            return

        if vc.members: 
            member_names = []
            for members in vc.members:
                nickname = members.display_name  # 닉네임 가져오기
                nickname = remove_emojis(nickname)  # 이모지 제거
                parts = nickname.split("/")
                if len(parts) > 1:
                    first = parts[0]
                    splittedfirst = first.split(" ")
                    if len(splittedfirst) >= 3:
                        member_names.append(splittedfirst[-1])
            output.append(f">{vc.name} 채널:\n" + "\n".join(member_names))

    await ctx.send("\n\n".join(output))

bot.run(os.environ['TOKEN'])