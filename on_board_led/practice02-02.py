import time
from machine import Pin

PIN_NO_LED = 2  # オンボードLEDのGPIO


def blink_led(pin, sleep_time_ms):
    """
    指定されたスリープ間隔でオンボードLEDを明滅させ、
    中断されるまで繰り返す。

    Parameters
    ----------
    pin : int
        設定対象のピン
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    """
    led = Pin(pin, Pin.OUT)

    try:
        while True:
            value = led.value()
            if value == 0:
                # 現在が消灯中であれば点灯させる
                led.on()
            else:
                # 現在が点灯中であれば消灯させる
                led.off()
            print(f'GPIO{pin}:{value}')  # 現在のピンの状態
            time.sleep_ms(sleep_time_ms)  # 指定ミリ時間、一時停止する

    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        led.off()
    
    return


if __name__ == "__main__":
    SLEEP_TIME_MS = 500
    blink_led(
        pin=PIN_NO_LED,
        sleep_time_ms=SLEEP_TIME_MS,
    )
