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
1. 対象のアプリケーションを実行する
   ```
   $ python <対象アプリケーション>
   ```
   - [Wiki-アプリケーション一覧](https://github.com/koba-masa/my_scraping_tool/wiki/%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E4%B8%80%E8%A6%A7)参照

### Dockerを利用する場合
1. `Docker`を起動する
   ```
   $ docker-compose build
   $ docker-compose up
   ```
1. 対象のアプリケーションを実行する
   ```
   $ docker-compose exec app poetry run python <対象アプリケーション>
   ```
   - [Wiki-アプリケーション一覧](https://github.com/koba-masa/my_scraping_tool/wiki/%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E4%B8%80%E8%A6%A7)参照

#### 注意事項
- Dockerコンテナ内からアクセスすることになるため、`localhost`を`host.docker.internal`に書き換える必要がある

## テスト実行手順
1. `Docker`を起動する
   ```
   $ docker-compose up -d
   ```
1. `pytest`を実行する
   ```
   $ poetry run pytest
   ```
