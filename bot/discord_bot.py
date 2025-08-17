import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ configの読み込み（ファイルがなければ初期化）
CONFIG_PATH = "config.json"

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "excluded_user_ids": [],
            "attack_channel_name": "攻撃VC",
            "defense_channel_name": "防衛VC"
        }

def save_config():
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(bot.config, f, indent=4, ensure_ascii=False)

bot.config = load_config()
bot.save_config = save_config

# ✅ Bot起動時のログ
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# ✅ Cogの読み込み（gaming.pyが cogs フォルダにある前提）
async def load_cogs():
    await bot.load_extension("cogs.gaming")

# ✅ Bot起動関数（main.pyから呼ばれる）
def run_bot():
    bot.loop.create_task(load_cogs())
    bot.run(os.getenv("DISCORD_TOKEN"))
