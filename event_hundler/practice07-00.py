import time
from machine import Pin

led = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN)

# 呼び出したい関数
def button_push(pin):
    print(f'PIN: {pin}, VALUE: {pin.value()}')
    led.on()
    time.sleep(1)
    led.off()

button.irq(trigger=Pin.IRQ_FALLING, handler=button_push)  # 値が0->1になったら関数を呼び出し

while True:
    time.sleep(1)
