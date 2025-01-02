# IoT練習: 08.Wi-Fiに接続してデータを送信してみよう

## 本練習の目的

- デバイスをネットワークに接続する
- HTTPの基本を理解する

ESP32は、Wi-FiやBluetoothを搭載しており、簡単に他のデバイスと通信したり、
サーバと通信したりすることが出来ます。

## 実装内容

仕様：Wi-Fiに接続して、Webサーバ（ http://192.168.4.1/ ）に自分の名前をJSON形式でPOST（送信）し応答結果を表示する

サーバはデータを受信すると時刻と合わせて送信内容を表示するので、正しく送られたかを確認しましょう。

データはJSONと呼ばれる形式であれば、なんでも受け取る状態となっているので、好きに試して下さい。

※ JSONは、データを簡単かつ効率的に交換するための軽量データ形式です。特にウェブアプリケーションでサーバーとクライアント間でデータを送受信するために広く使われています。

```json
{
  "name": "John",
  "age": 30,
  "isStudent": false
}
```

### Wi-Fi アクセスポイント

以下にテスト用のアクセスポイントを用意しました。(インターネットには接続していません。)

- SSID : intern2024
- PASSWORD : password2024

### Webサーバ仕様

以下のような仕様でWebサーバを作成してあります。

- IP : 192.168.4.1
- PORT : 5000
- POST URL : http://192.168.4.1:5000/
  - 入力：JSON
  - 出力：サーバの更新時刻
  - 動作：nameが入力に含まれていれば、サーバに保存している名前を更新する
- GET URL : http://192.168.4.1:5000/
  - 入力：Requestパラメータ（URLに?xxx=xxx&yyy=yyy形式で付与する）
  - 出力：サーバに保存された名前
  - 動作：サーバに保存された名前を返却する

※ 参考：サーバ側のソースコードは[こちら](server.py)
※ 参考：サーバを実行するアクセスポイント化したRaspberryのセットアップ手順は[こちら](setup.md)

## HTTPとは

"HTTP（HyperText Transfer Protocol）"は、ウェブブラウザとサーバー間でデータを送受信するためのプロトコルです。インターネット上でウェブページを表示するために使われる主要な通信手段です。

- クライアント：ウェブブラウザやモバイルアプリなど、ユーザーが操作する端末。
- サーバー：ウェブサイトのデータをホスティングしているコンピュータ。

## HTTPの基本動作

普段なれているネットは、以下のような流れで見れています。

1. クライアントがリクエストを送信 : ユーザーがウェブサイトにアクセスすると、クライアントがサーバーにリクエストを送ります。
1. サーバーがレスポンスを返す：サーバーはリクエストを受け取り、必要なデータを探し、クライアントにレスポンスを返します。
1. クライアントがデータを表示：クライアントは受け取ったレスポンスからデータを取り出して、ユーザーに提示します。

クライアントからのリクエストは以下の内容で構成されます。

- リクエストライン : HTTPメソッド、リクエストするURI、HTTPのバージョンから構成される
- ヘッダ : クライアントのソフトウェア情報、応答の形式の指定など
- ボディー : 後述のPOSTのみ存在、GETでは空
  
サーバが作成するレスポンスは以下の内容で構成されています。

- ステータス : サーバでの処理結果 
- ヘッダ : レスポンスの種類、大きさ、作成日など
- ボディー : ヘッダで定義された種類のデータ

## HTTPリクエストの種類

HTTPにはいくつかのリクエストメソッドがありますが、ここではGETとPOSTについて説明します。

### GETリクエスト

GETリクエストは、サーバーからデータを取得するために使われます。主に以下の特徴があります：

- データの取得：特定のリソース（例：ウェブページやAPIからのデータ）を取得する際に使用されます。
- URLにデータを含む：リクエストする際のパラメータはURLに付加されます。例：https://example.com/api?name=John&age=30
- セキュリティ面：URLにデータが含まれるため、機密情報の送信には適しません。

例えば、ホームページを表示する場合には、以下のようなファイル単位でこのGETリクエストが送信されています。

- HTMLファイル（ホームページの構造・テキスト）
- 表示する画像（jpg/pngファイルなど）
- 動かすためのスクリプト（jsファイルなど）
- レイアウト・デザイン情報（cssファイルなど）

### POSTリクエスト

POSTリクエストは、サーバーにデータを送信するために使われます。主に以下の特徴があります：

- データの送信：フォームの送信やデータのアップロードなど、サーバーに新しいデータを送信する際に使用されます。
- 本文にデータを含む：送信するデータはリクエストの本文に含まれ、URLには表示されません。
- セキュリティ面：GETリクエストに比べて、データがURLに表示されないため、より安全にデータを送信できます。

例えば、ショッピングサイトへのログイン情報・購入処理など他者に閲覧されたくない情報はPOSTリクエストで送信されています。

### ブラウザを使ってHTTPを見てみよう

Webブラウザのデベロッパツールを起動して（Ctl + Shift + I）、"Network"を選択してください。右側に以下のように表示されることを確認してください。

<image src="devtool.png" width="500px">

アドレスバーに以下のURLを入力してEnterを押してみましょう。

- https://httpbin.org/get

以下のような表示が確認できると思います。これは、サーバ"httpbin.org"に対して、"/get"というGETリクエストを送信したところ、200 OKという結果と、データが返却されたことを示しています。

<image src="get.png" width="400px">

次に、以下のURLをアドレスバーに入力するとダミーのピザオーダーの画面が開きます。

- https://httpbin.org/forms/post

<image src="post_request.png" width="400px">

データを入力して、"Submit Order"のボタンを押すと以下のようにPOSTリクエストが送信されたことがわかります。ここで、Payloadのタブを選択すると送信されたデータを確認することが出来ます。

<image src="post_header.png" width="400px">

画面で入力した値が、サーバに送られていることが確認できます。

<image src="post_payload.png" width="400px">

普段利用している色々なWebサイトがどのようなやりとりを裏で行っているか確認してみるのもいいでしょう、きっと膨大な量のリクエストとレスポンスに驚くかと思います。

- https://www.google.com
- https://www.amazon.com
- https://www.youtube.com/

以上はブラウザを利用した例でしたが、本項では画面を介さずにデータのやり取りのみを実装してもらいます。

## 以下を実行して結果を確認してみましょう

Wi-Fiへの接続

```python
import time
import network

SSID = 'intern2024'       # Wi-FiのSSID
PASSWORD = 'password2024'  # Wi-Fiのパスワード

wlan = network.WLAN(network.STA_IF)  # ステーションインターフェース（STAモード）で初期化
wlan.active(True)  # チップを起動
wlan.connect(SSID, PASSWORD)  # Wi-Fiアクセスポイントへ接続
while not wlan.isconnected():  # 接続状態になるまでループして待機
    print('Connecting to network...')
    time.sleep(1)
print('Network connected:', wlan.ifconfig())
```

WebサーバからGETリクエストによるデータの取得

```python
import urequests  # HTTP通信をするライブラリをインポート

url = 'http://192.168.4.1:5000/'  # GETリクエストを送信するURL
response = urequests.get(url)  # GETリクエストの送信

print('Response status:', response.status_code)  # GET処理結果
print('Response content:', response.text)  # サーバから返却されたデータ
```

WebサーバからGETリクエストによるデータの送信（GETのパラメータはスペースを受け付けないので気を付けましょう。）

```python
import urequests

# GETでパラメータを送る際には、URLにデータが入ります。
url = 'http://192.168.4.1:5000/?name=KATO-WORKS&age=129' 
response = urequests.get(url)  # GETリクエストの送信

print('Response status:', response.status_code)  # GET処理結果
print('Response content:', response.text)  # サーバから返却されたデータ
```

WebサーバへのPOSTデータの送信

```python
import urequests

url = 'http://192.168.4.1:5000/'  # POSTリクエストを送信するURL

# サーバに送信するデータ
data = {
    'name': 'KATO-WORKS',
}
response = urequests.post(url, json=data)  # POSTリクエストによるデータの送信

print('Response status:', response.status_code)  # POST処理結果
print('Response content:', response.text)  # サーバから返却されたデータ
```

[トップへ戻る](../README.md)
