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
        "\U0001F900-\U0001F9FF"  # 🤐 ~ 🧿 (추가 이모지)
        "\U0001FA00-\U0001FA6F"  # 🨀 ~ 🩯 (확장 이모지)
        "\U0001FA70-\U0001FAFF"  # 🩰 ~ 🫿 (최신 이모지, 🪙 포함)
        "\U00002600-\U000026FF"  # ☀ ~ ⛿ (기타 기호)
        "\U00002700-\U000027BF"  # ✀ ~ ➿ (딩밧)       
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

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
                nickname = remove_emojis(nickname)  # 이모지 제거
                parts = nickname.split("/")
                if len(parts) > 1:
                    first = parts[0]
                    splittedfirst = first.split(" ")
                    if len(splittedfirst) >= 2:
                        member_names.append(splittedfirst[-1])
            output.append(f"{vc.name}\n" + "\n".join(member_names))

    await ctx.send("\n\n".join(output))

bot.run(os.environ['TOKEN'])