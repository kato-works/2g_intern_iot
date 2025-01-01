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
    try:
        response = urequests.post(url, json=data)
        print('Response status:', response.status_code)

        if response.status_code != 200:  # HTTPは200が成功のコード
            print(f'POST Failed.')
            return None
        else:
            print('Response content:', response.text)
        return response.text
        
    except Exception as e:
        print(f'POST Failed. {e}')
        return None


if __name__ == "__main__":
    # Wi-Fiに接続
    wlan = connect_wifi(SSID, PASSWORD)
    # ５回繰り返して、カウントアップした数字を送信する。
    for count in range(5):
        # 送信データ
        data = {
            'name': 'KATO-WORKS',
            'count': count,
        }
        # サーバへ送信
        response = post_data(URL, data)
        time.sleep(1)

    # WiFiから切断
    wlan.disconnect()
