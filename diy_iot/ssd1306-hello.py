import time
from machine import Pin, I2C
# ESP32側に、ssd1306.pyを保存する必要がある
import ssd1306

# ESP32のI2Cピンを設定 (SCL=GPIO22, SDA=GPIO21)
i2c = I2C(scl=Pin(22), sda=Pin(21))

# ディスプレイの初期化 (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# ディスプレイをクリア
oled.fill(0)

# テキストを表示
oled.text("Hello, World!", 0, 0)
oled.text("ESP32 I2C OLED", 0, 10)

# ディスプレイに表示
oled.show()

time.sleep(1)

oled.fill(0)
oled.show()

