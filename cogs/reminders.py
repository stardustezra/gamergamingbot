import discord
from discord.ext import commands
import datetime

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_session_times = []

    @commands.command()
    async def remind(self, ctx, time, *, message):
        # Implement reminder functionality here
        # You can use the same logic as in bot.py to schedule reminders
        await ctx.send(f"Reminder set for {time}: {message}")

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
