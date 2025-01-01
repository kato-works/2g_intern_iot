import time
import random
from machine import ADC, Pin

# ADCピンの設定 (例えばGPIO34)
adc = ADC(Pin(34))
# ADCの幅を設定（通常は10ビット幅で0〜1023）
adc.width(ADC.WIDTH_10BIT)
# ADCの減衰を設定（デフォルトは0dB）
adc.atten(ADC.ATTN_11DB)  # 11dB attenuation (0-3.6V)

def print_range_bar(
    value, 
    max_value = 100.0, 
    prefix = 'Volume:', 
    suffix = '', 
    length = 50, 
    fill='█', 
    print_end="\r"):
    """
    バーグラフの表示

    Parameters
    ----------
        value : 現在の値
        prefix (str): バーの前に表示する文字列
        suffix (str): バーの後に表示する文字列
        length (int): バーの長さ
        fill (str): バーの中を埋める文字
        print_end (str): 最後に表示する文字列（デフォルトは '\r'）
    """
    # ％の計算
    percent = ("{0:.1f}").format(100 * (value / float(max_value)))
    # バーの長さの計算
    filled_length = int(length * value / max_value)
    # バーの文字列組み立て
    bar = fill * filled_length + '-' * (length - filled_length)
    # 表示
    print(f'{prefix} |{bar}| {percent}% {suffix}', end=print_end)

while True:
    # ADC値の読み取り
    value = adc.read()
    print_range_bar(value, max_value=1023, prefix='GPIO34', print_end='')
    time.sleep(0.2)
