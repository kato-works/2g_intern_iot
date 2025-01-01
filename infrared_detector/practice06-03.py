from machine import Pin
import time

PIN_NO_SENSOR = 4  # センサーのOUTと接続したGPIO

count = 0  # センサーの反応した回数


def sensor_trigger(pin):
    """
    センサーがONまたはOFFに遷移したときに、割り込み処理として呼ばれる

    Parameters
    ----------
    pin : Pin
        対象のGPIOピン
    """
    global count  # グローバルで変数を利用する宣言
    if pin.value() == 1:
        count = count + 1  # 反応した回数をインクリメント
        print(f'Pin ON: {count}')
    else:
        print('Pin OFF.')
    
    return


def set_trigger(pin_no):
    """
    対象のGPIOピンに割り込み処理を設定する

    Parameters
    ----------
    pin_no : int
        対象のGPIOピン番号
    """
    # GPIOピンの設定（例：GPIO 5）
    pin = Pin(pin_no, Pin.IN)
    # 割り込みの設定（ピンが立ち上がるときに割り込みを発生）
    pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=sensor_trigger)

    return


if __name__ == "__main__":
    set_trigger(pin_no=PIN_NO_SENSOR)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
