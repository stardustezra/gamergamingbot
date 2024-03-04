import asyncio

class ReminderManager:
    def __init__(self):
        self.reminders = {}

    async def create_reminder(self, user_id, time, message):
        if user_id not in self.reminders:
            self.reminders[user_id] = []

        reminder_time = int(time)
        self.reminders[user_id].append((reminder_time, message))
        await asyncio.sleep(reminder_time)
        await self.send_reminder(user_id, message)

    async def send_reminder(self, user_id, message):
        # You would typically use the discord.py API to send a reminder message here
        # Example: await user.send(f"Reminder: {message}")
        print(f"Reminder for user {user_id}: {message}")

    def get_reminders(self, user_id):
        return [reminder[1] for reminder in self.reminders.get(user_id, [])]
