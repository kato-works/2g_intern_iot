import time
from machine import Pin
from machine import TouchPad

touch_pad = TouchPad(Pin(32))  # PIN32を、タッチパッドとして設定

while True:
    touch_value = touch_pad.read()  # タッチパッドの静電容量の読み込み
    print(f'Touch value:{touch_value}')
    time.sleep_ms(200)
