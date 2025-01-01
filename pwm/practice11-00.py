from machine import Pin, PWM
import time

# GPIOピンの番号を指定（例: 13番ピン）
pwm_pin = 13
led_pin = 12

# Pinオブジェクトを作成
led_pwm = Pin(pwm_pin, Pin.OUT)
led = Pin(led_pin, Pin.OUT)


# PWMオブジェクトを作成
pwm = PWM(led_pwm)

# PWMの周波数を設定（例: 500Hz）
pwm.freq(50)

# 明るさを徐々に変更するループ
while True:
    # LEDを徐々に明るくする
    led.on()
    for duty in range(0, 1024):
        pwm.duty(duty)
        time.sleep(0.002)
    # LEDを徐々に暗くする
    led.off()
    for duty in range(1023, -1, -1):
        pwm.duty(duty)
        time.sleep(0.002)

