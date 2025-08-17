from bot.discord_bot import GamingBot
from bot.config.settings import load_settings
from bot.keep_alive import keep_alive  # ← 追加！

if __name__ == "__main__":
    keep_alive()  # ← ダミーWebサーバー起動
    settings = load_settings()
    bot = GamingBot()
    bot.run(settings["DISCORD_TOKEN"])
