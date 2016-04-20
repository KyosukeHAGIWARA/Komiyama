#readme for Komiyama

##overview
こみやまの誕生日をお祝いすることを目的に作られたスクリプト。  
tweepyでstreamingAPIを使っているから落ちない限りずっとTLを見張っててくれる

###Komiyama.py
メインなスクリプト。TLの監視、反応、イベントの管理などぜんぶごっちゃ煮。あんまりおいしくなさそう。

###getBirthday.py
twitterのAPI経由ではユーザーの設定した誕生日情報がとってこれない。  
無理矢理プロフィールページをスクレイピングしてとってくる。  
そもそも全員に公開で誕生日情報を設定しているtwitterユーザーそんなにいないでしょ。

##Usage
前提)  
twitterのOAuthを突破しなければならないので各個人でこんしゅーまーきーなりあくせーすとくーんなりを生成するといいと思う。    
生成したら  
```twitter.ini
[Twitter]
CK=xxxxxxxxxxxxxxxxxxxxxx
CS=xxxxxxxxxxxxxxxxxxxxxx
AT=xxxxxxxxxxxxxxxxxxxxxx
AS=xxxxxxxxxxxxxxxxxxxxxx
```
ってファイルを作ると動く。自分だけのbotにできるね。
