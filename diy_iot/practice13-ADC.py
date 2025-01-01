from machine import Pin, ADC
import time

# ADCピンの設定
adc_pin = ADC(Pin(32))  # GPIO32を使用
adc_pin.atten(ADC.ATTN_11DB)  # フルレンジの電圧（0Vから3.3V）を測定
adc_pin.width(ADC.WIDTH_12BIT)  # 12ビットの解像度を設定

while True:
    adc_value = adc_pin.read()  # ADC値を読み取る（0から4095の範囲）
    
    # ADC値を電圧に変換
    voltage = adc_value * 3.3 / 4096
    
    print("ADC Value: {}, Voltage: {:.2f}V".format(adc_value, voltage))
    time.sleep(1)  # 1秒待機