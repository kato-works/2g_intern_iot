import time
from machine import Pin
from machine import TouchPad

# 状態監視するピンの一覧
pin_no_list = [2, 4, 15, 13, 12, 14, 27, 33, 32]


def read_value(touch_pad: TouchPad):
    """
    TouchPadの値の読み込み（エラーハンドル用）
    エラー発生時には-1を値として返却

    Parameters
    ----------
    touch_pad : TouchPad
        計測対象のタッチパッド
    """
    try:
        touch_value = touch_pad.read()
    except ValueError:
        touch_value = -1

    return touch_value


def read_touch_pad_all(sleep_time_ms: int = 200):
    """
    全TouchPadの状態を確認

    Parameters
    ----------
    sleep_time_ms : int
        計測間隔
    """
    touch_pad_list = []  # TouchPadの一覧を格納
    for pin_no in pin_no_list:
        touch_pad = TouchPad(Pin(pin_no))
        touch_pad_list.append(touch_pad)
    
    try:
        count = 0
        while True:
            values = []
            for touch_pad in touch_pad_list:
                value = read_value(touch_pad)
                values.append(value)
            count += 1
            if count == 5:
                print(f'TouchPad: {pin_no_list}')
                count = 0
            print(f'Values: {values}')
    except KeyboardInterrupt:
        print("例外'KeyboardInterrupt'を捕捉")
    
    return


if __name__ == "__main__":
    read_touch_pad_all()
