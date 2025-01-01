import time
from machine import Pin
from machine import TouchPad

PIN_NO_TOUCH = 32  # 静電容量を見るピンのGPIO


def read_touch_pad(pin, sleep_time_ms):
    """
    指定されたスリープ間隔でTouchPadの静電容量を読み込む、
    中断されるまで繰り返す。

    Parameters
    ----------
    pin : int
        設定対象のピン
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    """

    touch_pad = TouchPad(Pin(pin))  # PIN32を、タッチパッドとして設定

    while True:
        touch_value = touch_pad.read()  # タッチパッドの静電容量の読み込み
        print(f'Touch value:{touch_value}')
        time.sleep_ms(sleep_time_ms)


if __name__ == "__main__":
    SLEEP_TIME_MS = 200
    read_touch_pad(
        pin=PIN_NO_TOUCH,
        sleep_time_ms=SLEEP_TIME_MS,
    )
