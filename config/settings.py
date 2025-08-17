import os

def load_settings():
    settings = {
        "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN")
    }

    if not settings["DISCORD_TOKEN"]:
        raise ValueError("❌ DISCORD_TOKEN is not set in environment variables.")

    return settings
