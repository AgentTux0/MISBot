import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

intents = discord.Intents.default()

client = Client(intents=intents)
client.run()
