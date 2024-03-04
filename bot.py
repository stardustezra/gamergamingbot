import discord
from discord.ext import commands
import json

# Load token from config file
with open('config.json') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']

# Define intents and enable required intents
intents = discord.Intents.all()
intents.message_content = True  # THIS IS IMPORTANT
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Import the reminders cog from the cogs folder
from cogs import reminders

# Load the reminders cog
bot.add_cog(reminders.Reminders(bot))

# Event: Bot is ready
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Run the bot with its token
bot.run(TOKEN)
