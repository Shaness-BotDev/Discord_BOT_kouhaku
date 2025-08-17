# Python 3.11 slim イメージで軽量かつ高速
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存ファイルをコピー
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# Botを起動
CMD ["python", "bot/discord_bot.py"]
