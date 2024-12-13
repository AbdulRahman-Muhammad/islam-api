from islam_web import get_fatwa
import discord

TOKEN = 'MTI4MTU4MTQwMjk2OTg3MDM3Nw.Guval7.ANnQXyy_jwccCe_PCiu0s0koJ3vWI-FoyxrrIE'
USER_ID = '1281581402969870377'

intents = discord.Intents.default()
intents.dm_messages = True  # Allow direct messages

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    for i in range(100000):
        response = get_fatwa(i)
        if response["ok"] == True:
            user = await bot.fetch_user(USER_ID)
            await user.send(response)
            print(f"Message sent for ID {i}: {response}")

bot.run(TOKEN)
