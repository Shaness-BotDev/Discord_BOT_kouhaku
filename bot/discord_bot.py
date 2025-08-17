import discord
from discord.ext import commands
import logging
import json
from pathlib import Path

# 🔌 Render Free Tier対応：ダミーWebサーバー起動
from keep_alive import keep_alive
keep_alive()

from bot.commands.gaming import GamingCommands

class GamingBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        intents.guilds = True
        intents.members = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None,
            case_insensitive=True
        )

        self.logger = logging.getLogger(__name__)
        self.config_path = Path("config/settings.json")
        self.config = self._load_config()

    def _load_config(self):
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"default_prefix": "!"}

    def save_config(self):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    async def setup_hook(self):
        await self.add_cog(GamingCommands(self))

    async def on_ready(self):
        print(f"✅ Logged in as {self.user}")
        print(f"📡 Connected to {len(self.guilds)} guild(s)")

# 🧠 Botインスタンス生成＆起動
if __name__ == "__main__":
    bot = GamingBot()
    bot.run(bot.config.get("DISCORD_TOKEN"))
