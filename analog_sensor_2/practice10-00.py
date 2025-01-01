import time
import random
from machine import ADC, Pin

# ADCピンの設定 (例えばGPIO34)
adc = ADC(Pin(34))
# ADCの幅を設定（通常は10ビット幅で0〜1023）
adc.width(ADC.WIDTH_10BIT)
# ADCの減衰を設定（デフォルトは0dB）
adc.atten(ADC.ATTN_11DB)  # 11dB attenuation (0-3.6V)


def print_range_bar(value, max_value):
    percent = int(100.0 * value / max_value)
    length = 30
    bar_length = int(30 * value / max_value)
    print('█' * bar_length + ' ' * (length - bar_length) + f' : {percent} %')

while True:
    # ADC値の読み取り
    value = adc.read()
    print_range_bar(value, max_value=1023, prefix='GPIO34', print_end='\n')
    time.sleep(0.2)
