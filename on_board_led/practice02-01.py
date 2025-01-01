import time
from machine import Pin

PIN_NO_LED = 2  # オンボードLEDのGPIO


def blink_led(sleep_time_ms):
    """
    指定されたスリープ間隔でオンボードLEDを明滅させ、
    中断されるまで繰り返す。

    Parameters
    ----------
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    """
    led = Pin(PIN_NO_LED, Pin.OUT)

    try:
        while True:
            led.on()  # LEDを点灯する
            time.sleep_ms(sleep_time_ms)  # 指定ミリ時間、一時停止する
            led.off()  # LEDを消灯する
            time.sleep_ms(sleep_time_ms) 

    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        led.off()
    
    return


if __name__ == "__main__":
    SLEEP_TIME_MS = 500
    blink_led(
        sleep_time_ms=SLEEP_TIME_MS,
    )
