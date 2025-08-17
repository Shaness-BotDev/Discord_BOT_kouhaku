from bot.discord_bot import GamingBot
import os

if __name__ == "__main__":
    bot = GamingBot()
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
