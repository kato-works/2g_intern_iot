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
1. クライアントがデータを表示：クライアントは受け取ったデータを処理し、ユーザーに表示します。

## HTTPリクエストの種類

HTTPにはいくつかのリクエストメソッドがありますが、ここではGETとPOSTについて説明します。

### GETリクエスト

GETリクエストは、サーバーからデータを取得するために使われます。主に以下の特徴があります：

- データの取得：特定のリソース（例：ウェブページやAPIからのデータ）を取得する際に使用されます。
- URLにデータを含む：リクエストする際のパラメータはURLに付加されます。例：https://example.com/api?name=John&age=30
- セキュリティ面：URLにデータが含まれるため、機密情報の送信には適しません。

### POSTリクエスト

POSTリクエストは、サーバーにデータを送信するために使われます。主に以下の特徴があります：

- データの送信：フォームの送信やデータのアップロードなど、サーバーに新しいデータを送信する際に使用されます。
- 本文にデータを含む：送信するデータはリクエストの本文に含まれ、URLには表示されません。
- セキュリティ面：GETリクエストに比べて、データがURLに表示されないため、より安全にデータを送信できます。

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

WebサーバからGETリクエストによるデータの送信

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
