import discord
from discord.ext import commands
import datetime
import asyncio

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_session_times = []

    @commands.command()
    async def remind(self, ctx, time_str, *, message):
        try:
            # Parse the time string to get the reminder time
            reminder_time = datetime.datetime.strptime(time_str, "%d-%m-%Y %H:%M")
        except ValueError:
            await ctx.send("Invalid time format. Please use DD-MM-YYYY HH:MM.")
            return

        # Calculate the time difference until the reminder
        delta = (reminder_time - datetime.datetime.now()).total_seconds()

        if delta <= 0:
            await ctx.send("Reminder time should be in the future.")
            return

        # Schedule the reminder task
        await self.schedule_reminder(ctx, delta, message)

    async def schedule_reminder(self, ctx, delta, message):
        # Wait for the specified time
        await asyncio.sleep(delta)

        # Send the reminder message
        await ctx.send(f"Reminder: {message}")

    @remind.error
    async def remind_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide both a time and a message for the reminder.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided. Please use the correct time format (DD-MM-YYYY HH:MM).")

    @commands.command()
    async def lastsession(self, ctx):
        if self.last_session_times:
            last_sessions_str = '\n'.join(str(time) for time in self.last_session_times)
            await ctx.send(f"The last 2 session times were:\n{last_sessions_str}")
        else:
            await ctx.send("No session times recorded.")

    # Add more reminder-related commands as needed

def setup(bot):
    bot.add_cog(Reminders(bot))
