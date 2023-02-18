# my_scraping_tool
汎用的なスクレイピングツール

## 機能概要
|機能名|機能概要|設定ファイル|出力ファイル|備考|
|:--|:--|:--|:--|:--|
|`http_status`|対象URLのHTTPステータスコードを取得する|`config/urls.txt`|`'tmp/result/{0}_http_status_getter.csv'`|`{0}`・・・※1|
|`element_value`|対象URLのCSSセレクタにて指定した要素値・属性値を取得する|`config/urls.txt`</br>`config/css_selector.csv`|`tmp/result/{0}_element_value_getter.csv`|`{0}`・・・※1|

※1・・・`YYYYMMDD_HHMMSS`の形式

## 実行手順
### Docker起動手順
1. `Docker`を起動する
   ```
   $ docker-compose build
   $ docker-compose up
   ```

### アプリケーション実行手順
1. 必要なライブラリをインストールする
   ```
   $ docker-compose run --rm app poetry install
   ```

1. 設定ファイルを用意する
   - 必要な設定ファイルは[機能概要](#機能概要)を参照

1. アプリケーションを実行する
   ```
   $ docker-compose run --rm app poetry run python my_scraping_tool <機能名>
   ```

   - 機能名は[機能概要](#機能概要)を参照

### テスト実行手順
1. 必要なライブラリをインストールする
   ```
   $ docker-compose run --rm app poetry install
   ```
1. アプリケーションを実行する
   ```
   $ docker-compose run --rm app poetry run pytest
   ```

#### 注意事項
- Dockerコンテナ内からアクセスすることになるため、`localhost`を`host.docker.internal`に書き換える必要がある
