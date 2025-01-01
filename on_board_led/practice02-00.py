import time
from machine import Pin

led = Pin(2, Pin.OUT)

while True:
    led.on()  # LEDを点灯する
    time.sleep_ms(500)  # 指定ミリ時間、一時停止する
    led.off()  # LEDを消灯する
    time.sleep_ms(500) 
