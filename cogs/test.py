import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta

class Reminder(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def remind(self, ctx, date: str, time: str, *, reminder_text: str):
        try:
            # Parse the provided date and time into a datetime object
            reminder_datetime = datetime.strptime(f"{date} {time}", "%d %m %Y %H:%M")
        except ValueError:
            # If the format is invalid, send an error message
            await ctx.send("Invalid date/time format. Please use DD MM YYYY HH:MM format.")
            return

        # Get the current datetime
        current_datetime = datetime.now()
        # Calculate the time difference between the reminder datetime and the current datetime
        time_difference = reminder_datetime - current_datetime

        # Ensure that the reminder time is in the future
        if time_difference.total_seconds() <= 0:
            await ctx.send("The reminder time must be in the future.")
            return

        # Send a message to @everyone with the reminder details
        await ctx.send(f"@everyone, I'll remind you on {reminder_datetime.strftime('%d %B %Y, %H:%M')}: {reminder_text}")
        # Sleep for the duration until the reminder datetime
        await asyncio.sleep(time_difference.total_seconds())
        # Send a reminder message to @everyone
        await ctx.send(f"@everyone, Reminder: {reminder_text}")

async def setup(client):
    await client.add_cog(Reminder(client))
