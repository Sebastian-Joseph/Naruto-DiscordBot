import discord
import random
import time
import asyncio

client = discord.Client()
TOKEN = "Nzk4NDI5MzA4NTg2MDMzMTgz.X_05PQ.WHKB1U_O0RZdQ4Iourk-soXZZzg"
#not the token anymore so don't even try it

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Naruto!"):

        if str(message.author) == "Seb#3204":
            await message.channel.send("Hello Master!")
        else:
            await message.channel.send("Believe It!")

client.run(TOKEN)
