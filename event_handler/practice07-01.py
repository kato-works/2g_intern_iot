import time
from machine import Pin

PIN_NO_LED = 2  # オンボードLEDのGPIO
PIN_NO_BUTTON = 0  # オンボードボタンのGPIO

led = None


def set_event(led_pin_no=2, button_pin_no=0):
    """
    PINにイベントを設定

    Parameters
    ----------
    led_pin_no : int
        LED割り当てピン
    button_pin_no : int
        BUTTON割り当てピン
    """
    global led
    led = Pin(led_pin_no, Pin.OUT)
    button = Pin(button_pin_no, Pin.IN)
    button.irq(trigger=Pin.IRQ_FALLING, handler=button_push)

    return


def button_push(pin):
    """
    BUTTONが押された際の処理、
    LEDを１秒点灯する

    Parameters
    ----------
    pin : Pin
        イベントが発生したピン（ボタン）
    """
    print(f'PIN: {pin}, VALUE: {pin.value()}')
    led.on()
    time.sleep(1)
    led.off()

    return


if __name__ == "__main__":
    set_event(led_pin_no=PIN_NO_LED, button_pin_no=PIN_NO_BUTTON)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        if led is not None:
            led.off()
