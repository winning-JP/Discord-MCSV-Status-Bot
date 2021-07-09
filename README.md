# Discord-MCSV-Status-Bot# Minecraft-Server-Status-Bot

### 動作環境
| OS | Windows 10 |
|:---|:---|
| Python | 3.9.4 |
| discord.py | 1.7.3 |
| requests | 2.25.1 |

## 使用方法

### 事前準備
1. Discordのトークン
    1. まずはじめに[Discord Developer Portal](https://discord.com/developers/applications/)にアクセスして、「Create New App」をクリック
    2. アプリケーションの名前(適当でもOK)を決めて「Create」をクリックして作成する
    4. 作成したら「Bot」をクリックしてBuild-A-Botの「Add Bot」をクリック
    5. ADD A BOT TO THIS APP?(このアプリにボットを追加しますか？)と聞かれるので「Yes, do it!」をクリックしてください
    7. BOTを追加したらTOKENの下にある「Click to Reveal Token」をクリックしてトークンを表示させて表示されたトークンをコピーするかその下にある「Copy」をクリックしてBOTのトークンをコピーしてください  
      ・BOTのアイコンを変更したい場合は、ICONの下にあるアイコンをクリックして変更してください。  
      ・BOTの名前を変更したい場合は、USERNAMEの下にあるテキストボックスをクリックして変更してください。  
2. Pythonの実行できる環境
---
### BOTのトークンを変更
1.DiscordのBOTのトークンを準備する

2.トークンを書く

ソースコードをそのまま利用した場合は31行目にある
~~~
client.run('DISCORD-BOT-TOKEN')
~~~

**DISCORD-BOT-TOKEN**の部分を消して最初に用意したトークンに置き換える

---
### ServerのIP・ポート番号を変更
ソースコードをそのまま利用した場合は8行目にある
~~~
r = requests.get('https://api.minetools.eu/ping/[SERVER-IP-ADDRESS]/[PORT]')
~~~
上記のコードにある[SERVER-IP-ADDRESS]と[PORT]の部分を変更して使用してください。

サーバーのIPアドレス＝[SERVER-IP-ADDRESS]  
サーバーのポート番号＝[PORT]

>例)Hypixelの場合
~~~
r = requests.get('https://api.minetools.eu/ping/mc.hypixel.net/25565')
~~~

---
### BOTのコマンドを変更

最初の「!」を変えたい場合
ソースコードをそのまま利用した場合は行目にある
~~~
client = commands.Bot(command_prefix="!")
~~~
...(command_prefix="!")の中にある「!」を他の物に変更する  

>例)!を?にしたい場合
~~~
client = commands.Bot(command_prefix="?")
~~~

### コマンドのキーワードを変えたい場合
ソースコードをそのまま利用した場合は7行目にある
~~~
async def mcst(ctx):
~~~
上記のコードにある**mcst**の部分を好きなコマンドに変更してください  
>例)!statusにしたい場合
~~~
async def status(ctx):
~~~
---
### サーバーのバージョンの記載方法の変更
ソースコードをそのまま利用した場合、直書きでバージョンを表示するようにしてます  
APIを返してバージョンを取得する場合は少し変更する必要があります

ソースコードをそのまま利用した場合は18行目と19行目にあるコードを変更する必要があります
>18行目
~~~
#description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン:' + Version,
~~~
>19行目
~~~
description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: 1.17.x', 
~~~

#### APIを返してバージョンを記載する場合は  
18行目のコメントアウトを消して19行目の先頭にコメントアウトしてください。
~~~
description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン:' + Version,
#description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: [任意のバージョン]',
~~~
#### APIを返してバージョンを記載したくない場合は  
18行目の先頭にコメントアウトして19行目のコメントアウトを消してください。
また、バージョンの記載方法は
>19行目
~~~
#description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: [任意のバージョン]',
~~~
[任意のバージョン]の部分を変更してください。
>例)Minecraft Serverのバージョンが1.17.1の場合
~~~
#description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン:' + Version,
description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: 1.17.1',
~~~
>例)APIを返してMinecraft Serverのバージョンを取得する場合
~~~
description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン:' + Version,
#description='最大接続可能人数: ' + max + '\n現在の参加人数: ' + online + '\nサーバーのバージョン: [任意のバージョン]',
~~~

---
### 利用しているAPIについて
BOTに使用しているAPIは、[MineTools](https://api.minetools.eu/)のPingのAPIを使用しています。
### APIの利用方法
> ※PythonやAPI自体ついこの間触れたばかりなので間違ってることを言ってるかもです...なので分かる範囲で解説？していきます
コードの書き方としては、Pythonで記載している感じで書いていきます。

> サーバーのMOTD
`["description"]`

> サーバーのアイコン
> ※base64を画像へ変換する必要があります。（自分にはワケワカメ状態）
`["favicon"]`

> レイテンシ...ん？（なにそれ）
`["latency"]`

> サーバーに入れる最大人数
`["players"]["max"]`

> サーバーに参加してる人数
`["players"]["online"]`

> サーバーに参加してるプレイヤー（イマイチコードをどう書いたら良いかわかんなくてワケワカメ状態^^）
`["players"]["sample"]`

> サーバーのバージョン
`["version"]["name"]`

> サーバーのプロトコル
`["version"]["protocol"]`

> SAMPLEコード①
~~~
description = str(json_data["description"])
favicon = str(json_data["favicon"])
latency = str(json_data["latency"])
max = str(json_data["players"]["max"])
online = str(json_data["players"]["online"])
sample  = str(json_data["players"]["sample"])
name  = srt(json_data["version"]["name"])
protocol  = str(json_data["version"]["protocol"])
~~~
> SAMPLEコード②
~~~
["description"]
["favicon"]
["latency"]
["players"]["max"]
["players"]["online"]
["players"]["sample"]
["version"]["name"]
["version"]["protocol"]
~~~

### BOTが送信するメッセージの変更
SAMPLEコードの一部を書いてみました。

※下のコードを使用する場合は上記のSAMPLEコードを加える必要があります。
~~~
description='サーバーのMOTD：' + description\n + 'サーバーに入れる最大人数：' + max\n + 'サーバーに参加してる人数：' + online\n + 'サーバーのバージョン：' + name\n,
~~~
---
## 疲れた。
恐らくこのコードをカスタマイズなどをすればきっと良いBOTが作れると思います！
Minecraft以外のAPIを使用することも可能ですが、設定は別途必要ですけで自由度はアップ！！

参考に下記事

> [MineTools WebSite](https://api.minetools.eu/ping/)
> 
> [Mignon Style / Markdown記法 チートシート GitHub](https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa)
> 
> [こうちゃの日常 GitHub](https://github.com/ko-cha/sample)
> 
> [こうちゃの日常 YouTube](https://www.youtube.com/watch?v=-qCKz01qJxA)
>
> [Robotic Nation YouTube](https://youtu.be/7r1Jur8o_Cw)
