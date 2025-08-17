# Pythonの軽量イメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# プロジェクトファイルをすべてコピー
COPY . .

# 依存ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Botを起動
CMD ["python", "main.py"]
