# my_scraping_tool
汎用的なスクレイピングツール

## 事前準備
- `poetry`のインストールを行う
   ```
   $ pip install poetry
   ```
   - Docker環境を利用する場合は・・・

## 実行手順
### ホストOSにpythonの環境が整っている場合
1. 環境変数`PYTHONPATH`に上位階層を読み込めるようにするため、親ディレクトリを設定する
   ```
   $ export PYTHONPATH="..:$PYTHONPATH"
   ```
1. 必要なライブラリのインストールを行う
   ```
   $ poetry install
   ```

### Dockerを利用する場合
1. `Docker`を起動する
   ```
   $ docker-compose up -d
   ```

## テスト実行手順
1. `Docker`を起動する
   ```
   $ docker-compose up -d
   ```
1. `pytest`を実行する
   ```
   $ poetry run pytest
   ```
