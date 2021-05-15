# scrapy,splash,mysql環境の作成ツール

[scrapy](https://scrapy.org/), [splash](https://splash.readthedocs.io/)を使用してスクレイピングし、mysqlにデータを保存する環境です。

## 環境情報
Docker Engine v20.10.5  
Docker Compose v1.28.5  
M1 Macで動作確認  

## サンプル実行
以下の手順でサンプルを実行できます。  
※以下のコマンドはルートで実行してください。

1. イメージ作成  
```
docker build . -t scrapy_env
```
タグ名をscrapy_envにすること。

2. .envの作成  
.sample_envをコピーして.envファイルを作成してください。  
MYSQLの環境情報は任意で変更可能です。   

3. DBの作成と実行環境の起動  
```
docker-compose up
```
DB環境: scrapy_mysql  
scrapy実行環境: scrapy_exec  
が作成されます。

4. 処理の実行  
  
scrapy実行環境の起動:  
```
docker exec -it scrapy_exec bash
```

サンプルコードの実行。  
サンプルコードは以下のサイトをスクレイピングします。  
https://quotes.toscrape.com/  
こちらの引用文を最後のページまでスクレイピングします。  
```
cd example
scrapy crawl quotes
```

DB環境のmysqlの  
データベース: scrapy  
テーブル: quotes  
にスクレイピングした内容が保存されています。  
## メモ
サンプルのタグをコンマ区切りで入れようとしていたができていない。  
フォルダーの構成などは追々記載する。  
