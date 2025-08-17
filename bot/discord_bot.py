import discord
from discord.ext import commands
from bot.config.settings import load_settings  # ← 安全な設定読み込み

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # VC機能を使うなら必要
intents.guilds = True
intents.members = True  # 必要に応じて

settings = load_settings()
TOKEN = settings["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("🔧 Bot is ready and operational.")

# 🔄 Cogのロード（例：VC機能や管理機能など）
initial_extensions = [
    "bot.cogs.voice",
    "bot.cogs.admin",
    "bot.cogs.games"
]

for ext in initial_extensions:
    try:
        bot.load_extension(ext)
        print(f"✅ Loaded extension: {ext}")
    except Exception as e:
        print(f"❌ Failed to load extension {ext}: {e}")

bot.run(TOKEN)
