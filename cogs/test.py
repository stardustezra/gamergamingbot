# ./cogs/responder.py
from discord.ext import commands

class Responder(commands.Cog):
    def __init__(self, client):
        self.client = client # sets the client variable so we can use it in cogs
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

async def setup(client):
    await client.add_cog(Responder(client))