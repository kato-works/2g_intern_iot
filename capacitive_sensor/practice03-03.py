import time
from machine import Pin
from machine import TouchPad

PIN_NO_TOUCH = 32  # 静電容量を見るピンのGPIO
PIN_NO_LED = 2  # オンボードLEDのGPIO


def read_touch_pad(touch_pin, led_pin, sleep_time_ms: int = 200, threshold: int = 150):
    """
    指定されたスリープ間隔でTouchPadの静電容量を読み込み、
    閾値以下であればLEDを点灯させ、
    中断されるまで繰り返す。

    Parameters
    ----------
    touch_pin : int
        タッチ設定対象のピン
    led_pin : int
        LED表示のピン
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    threshold : int
        タッチ判定の閾値（デフォルト150）
    """

    led = Pin(led_pin, Pin.OUT)
    touch_pad = TouchPad(Pin(touch_pin))  # PIN32を、タッチパッドとして設定

    try:
        while True:
            try:
                touch_value = touch_pad.read()
            except ValueError:  # ValueErrorが発生したら、-1を読み込み値に設定する
                touch_value = -1

            if touch_value == -1:
                print('Grouded...')
            elif touch_value <= threshold:
                led.on()
                print(f'Touched! ({touch_value})')
            else:
                led.off()
                print(f'No touch. ({touch_value})')
                
            time.sleep_ms(sleep_time_ms)

    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        led.off()
    
    return


if __name__ == "__main__":
    SLEEP_TIME_MS = 200
    read_touch_pad(
        touch_pin=PIN_NO_TOUCH,
        led_pin=PIN_NO_LED,
        sleep_time_ms=SLEEP_TIME_MS,
    )
