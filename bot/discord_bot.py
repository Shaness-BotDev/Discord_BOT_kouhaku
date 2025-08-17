import discord
from discord.ext import commands
from config.settings import load_settings  # ← これでOK！

class GamingBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.members = True

        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        try:
            await self.load_extension("bot.commands.gaming")
            print("✅ Loaded extension: bot.commands.gaming")
        except Exception as e:
            print(f"❌ Failed to load gaming cog: {e}")

    async def on_ready(self):
        print(f"✅ Logged in as {self.user} (ID: {self.user.id})")

def run_bot():
    settings = load_settings()
    token = settings["DISCORD_TOKEN"]
    bot = GamingBot()
    bot.run(token)
