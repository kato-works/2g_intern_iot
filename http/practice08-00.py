import time
import network
import urequests

SSID = 'intern2024'       # Wi-FiのSSID
PASSWORD = 'password2024'  # Wi-Fiのパスワード
URL = 'http://192.168.4.1:5000/'  # POSTリクエストを送信するURL


def connect_wifi(ssid, password):
    """
    Wi-Fiへ接続

    Parameters:
    ssid : str
        接続先のSSID
    password : str
        Wi-Fiのパスワード
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():  # 接続するまで待機
        print('Connecting to network...')
        time.sleep(1)
    print('Network connected:', wlan.ifconfig())
    return wlan


def post_data(url, data):
    """
    WebサーバへデータのPOST実行

    Parameters:
    url : str
        送信するサーバのURL
    data : dict
        送信するデータのDict
    """
    response = urequests.post(url, json=data)
    print('Response status:', response.status_code)
    print('Response content:', response.text)
    return response


# Wi-Fiに接続
wlan = connect_wifi(SSID, PASSWORD)

# 送信データ
data = {
    'name': 'KATO-WORKS',
}

# サーバへ送信
response = post_data(URL, data)

# WiFiから切断
wlan.disconnect()
