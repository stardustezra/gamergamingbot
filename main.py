# ./main.py
import asyncio
import discord
from discord.ext import commands
import os
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']

# Define intents and enable required intents
intents = discord.Intents.all()
intents.message_content = True
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix = "!", intents=intents)

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)
        
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

asyncio.run(main())