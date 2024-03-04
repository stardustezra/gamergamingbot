import discord
from discord.ext import commands
import json
from reminders import ReminderManager
from datetime import datetime

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
reminder_manager = ReminderManager()

# Command to set a reminder
@bot.command()
async def remind(ctx, when, *, message):
    reminder_time = parse_datetime(when)
    if reminder_time:
        await reminder_manager.create_reminder(ctx.author.id, reminder_time, message)
        await ctx.send(f"Reminder set for {reminder_time.strftime('%d-%m-%Y %H:%M:%S')}: {message}")
    else:
        await ctx.send("Invalid date/time format. Please use DD-MM-YYYY HH:MM:SS")

def parse_datetime(when):
    try:
        reminder_time = datetime.strptime(when, '%d-%m-%Y %H:%M:%S')
        if reminder_time < datetime.now():
            return None
        return reminder_time
    except ValueError:
        return None

# Command to view all reminders
@bot.command()
async def viewreminders(ctx):
    reminders = reminder_manager.get_reminders(ctx.author.id)
    if reminders:
        await ctx.send("Your reminders:")
        for reminder in reminders:
            await ctx.send(f"- {reminder}")
    else:
        await ctx.send("You have no reminders.")

# Event: Bot is ready
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Run the bot with its token
bot.run(TOKEN)
