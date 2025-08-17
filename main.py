from bot.discord_bot import GamingBot
from bot.config.settings import load_settings  # ← トークン取得！

if __name__ == "__main__":
    settings = load_settings()
    bot = GamingBot()
    bot.run(settings["DISCORD_TOKEN"])
