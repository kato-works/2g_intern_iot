import time
from machine import Pin

ir_sensor = Pin(4, Pin.IN)  # GPIO4を、入力ピンとして設定

while True:
    value = ir_sensor.value()  # ピンの値を読み込む
    print(f'ir_sensor: {value}')
    time.sleep_ms(1000)
