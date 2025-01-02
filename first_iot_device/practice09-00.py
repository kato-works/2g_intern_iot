import time
import network
import urequests

from machine import Pin

# サーバ設定
SSID = 'intern2024'       # Wi-FiのSSID
PASSWORD = 'password2024'  # Wi-Fiのパスワード
URL = 'http://192.168.4.1:5000/'  # POSTリクエストを送信するURL

PIN_NO_SENSOR_LED = 13
PIN_NO_IR_SENSOR = 4

led_sensor_detect = Pin(PIN_NO_SENSOR_LED, Pin.OUT)  # センサー反応中に点灯するLED
sensor = Pin(PIN_NO_IR_SENSOR, Pin.IN)  # 人感センサー


def sensor_triggerd(sensor_pin):
    """
    センサーが押されたら

    Parameters
    ----------
    sensor_pin : Pin
        トリガされたセンサーのピン
    """
    status = sensor.value()
    if status == 1:
        print('Sensor: ON')
        led_sensor_detect.on()
        data = {
            'name': 'KATO-WORKS',
            'AM312': 'ON',
        }
        response = post_data(URL, data)
    else:
        print('Sensor: OFF')
        led_sensor_detect.off()
        data = {
            'name': 'KATO-WORKS',
            'AM312': 'OFF',
        }
        response = post_data(URL, data)

    return


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

# Wi-Fiに接続
wlan = connect_wifi(SSID, PASSWORD)

sensor.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=sensor_triggerd) 

while True:
    time.sleep(1)

# WiFiから切断
wlan.disconnect()
