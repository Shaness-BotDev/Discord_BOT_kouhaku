import discord
from discord.ext import commands
from bot.config.settings import load_settings  # ← 環境変数読み込み

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

settings = load_settings()
TOKEN = settings["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("🎮 Bot is ready to game!")

# 🎮 Gaming Cog のロード
try:
    bot.load_extension("bot.commands.gaming")
    print("✅ Loaded extension: bot.commands.gaming")
except Exception as e:
    print(f"❌ Failed to load gaming cog: {e}")

bot.run(TOKEN)
