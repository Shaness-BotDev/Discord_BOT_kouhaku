from bot.keep_alive import keep_alive
from bot.discord_bot import run_bot

if __name__ == "__main__":
    keep_alive()     # Render用のダミーWebサーバー起動
    run_bot()        # Discord Bot起動
