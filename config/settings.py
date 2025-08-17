import os

def load_settings():
    """
    環境変数から設定を読み込む関数。
    今は Discord Bot のトークンのみ。
    """
    settings = {
        "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN")
    }

    if not settings["DISCORD_TOKEN"]:
        raise ValueError("❌ DISCORD_TOKEN is not set in environment variables.")

    return settings
