#readme for Komiyama

##overview
こみやま(@shh_y)の誕生日をお祝いすることを目的に作られたスクリプト。  
tweepyでstreamingAPIを使っているから落ちない限りずっとTLを見張っててくれる。  
TODOとかタスクとか記念日とかをフォーマットに従ってツイートすると勝手に解釈して勝手にDBに登録してそれっぽいタイミングでお知らせしてくれる(といいなぁ。)

###Komiyama.py
メインなスクリプト。TLの監視、反応、イベントの管理などぜんぶごっちゃ煮。あんまりおいしくなさそう。  
tweepyのstreamのつなぎ方もろもろはこの方のエントリを参考にした。  
[【Python3+MySQL+Twitter】ツイートからデータベースにデータを追加する](http://nnsnodnb.hatenablog.jp/entry/python3-mysql-twitter-todo)

###getBirthday.py
twitterのAPI経由ではユーザーの設定した誕生日情報がとってこれない。  
しょうがないので無理矢理プロフィールページをスクレイピングしてとってくる。  
そもそも全員に公開で誕生日情報を設定しているtwitterユーザーそんなにいないでしょ。

##Usage
前提)  
twitterのOAuthを突破しなければならないので各個人でこんしゅーまーきーなりあくせーすとくーんなりを生成するといいと思う。    
生成したら  
```python:twitter.ini
#twitter.ini
[Twitter]
CK=xxxxxxxxxxxxxxxxxxxxxx
CS=xxxxxxxxxxxxxxxxxxxxxx
AT=xxxxxxxxxxxxxxxxxxxxxx
AS=xxxxxxxxxxxxxxxxxxxxxx
```
ってファイルを作ると動く。自分だけのbotにできるね。

