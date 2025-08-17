import discord
from discord.ext import commands
import json
import os

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

def save_config(bot):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(bot.config, f, indent=4, ensure_ascii=False)

class CustomBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = load_config()
        self.save_config = lambda: save_config(self)

    async def setup_hook(self):
        await self.load_extension("cogs.gaming")  # ← Cogをここで読み込む

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = CustomBot(command_prefix="!", intents=intents)

def run_bot():
    bot.run(os.getenv("DISCORD_TOKEN"))
