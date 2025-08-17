import sys
import os

# 🔧 モジュールパスを追加して、Docker環境でも 'bot' を認識させる
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.commands.gaming import GamingCommands
from bot.config.settings import load_settings
from flask import Flask
import discord
from discord.ext import commands

# 🔧 Flask keep_alive サーバー（Render Free Tier対策）
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is alive!"

# 🔧 Discord Botの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 🔧 Cogの登録
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    bot.add_cog(GamingCommands(bot))

# 🔧 環境変数からトークンを取得
if __name__ == "__main__":
    import threading

    def run_flask():
        app.run(host="0.0.0.0", port=8080)

    threading.Thread(target=run_flask).start()

    TOKEN = os.getenv("DISCORD_TOKEN")
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ DISCORD_TOKEN not found in environment variables.")
