import time
from machine import Pin

PIN_NO_SENSOR = 4  # センサーのOUTと接続したGPIO


def read_pin(pin_num, sleep_time_ms):
    """
    指定されたスリープ間隔でPINの状態を読み込む、
    中断されるまで繰り返す。

    Parameters
    ----------
    pin_num : int
        読み込み対象のピン
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    """
    pin = Pin(pin_num, Pin.IN)  # 対象のPINを入力として設定

    while True:
        value = pin.value()
        print(f'GPIO{pin_num}: {value}')
        time.sleep_ms(sleep_time_ms)


if __name__ == "__main__":
    SLEEP_TIME_MS = 1000
    read_pin(
        pin_num=PIN_NO_SENSOR,
        sleep_time_ms=SLEEP_TIME_MS,
    )
