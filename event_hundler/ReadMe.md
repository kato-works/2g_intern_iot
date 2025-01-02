# IoT練習: 07.イベントハンドラを実装してみよう

## 本練習の目的

- 割り込みについて学ぶ
- 構造化されたプログラムを作成する

## 実装内容

仕様：イベントハンドラを使ってBOOTボタン操作を検出して、LEDの明滅を切り替える

ESP32では、ピンの状態変化を検出して関数を呼び出す、割り込みハンドラの実装が可能です。

```python
# pinに、Pin.IRQ_FALLINGが発生したら、関数handlerを呼び出す
pin.irq(trigger=Pin.IRQ_FALLING, handler=handler) 
```

- Pin.IRQ_FALLING は"1"から"0"に値が変わった際に、割り込みを生成します。
- Pin.IRQ_RISING は"0"から"1"に値が変わった際に、割り込みを生成します。

BOOTボタンのGPIOは0で、押された状態が"0"、離された状態が"1"です。

## 以下を実行して結果を確認してみましょう

イベントハンドラを使わずに実装するとどうなるでしょう。スリープ時間を変えて試してみましょう。

```python
import time
from machine import Pin

pin = Pin(0, Pin.IN)  # GPIO0に対して、入力を設定

prev_status = 1  # 前回の状態

while True:
    # 現在のピンの状態を取得
    status = pin.value()

    if prev_status != status:  # 前回のピン状態と比較し、変化したことを検出
        if status == 0:
            print('ON')
        else:
            print('OFF')
        # 今回のピン状態を保存
        prev_status = status

    time.sleep_ms(200)

```

ボタンが押されたときに反応

```python
import time
from machine import Pin

# 呼び出したい関数
def event(pin):
    print(f'ON: {pin}')

pin = Pin(0, Pin.IN)  # GPIO0に対して、入力を設定
pin.irq(trigger=Pin.IRQ_FALLING, handler=event)  # 値が1->0になったら関数を呼び出し

while True:
    time.sleep(1)
 
```

ボタンが離されたときに反応

```python
import time
from machine import Pin

# 呼び出したい関数
def event(pin):
    print(f'OFF: {pin}')

pin = Pin(0, Pin.IN)  # GPIO0に対して、入力を設定
pin.irq(trigger=Pin.IRQ_RISING, handler=event)  # 値が0->1になったら関数を呼び出し

while True:
    time.sleep(1)
 
```

ではこうなると？

```python
import time
from machine import Pin

# 呼び出したい関数
def event(pin):
    print(f'PIN: {pin}, VALUE: {pin.value()}')

pin = Pin(0, Pin.IN)  # GPIO0に対して、入力を設定
pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=event)  # 値が0->1もしくは、1->0になったら関数を呼び出し

while True:
    time.sleep(1)
 
```

１つのピンにイベントハンドラは１つしか設定できません。以下のように書くと何が起きるでしょうか

```python
import time
from machine import Pin

def event_rising(pin):
    # 表示されるか確認しよう
    print(f'event_rising: PIN: {pin}, VALUE: {pin.value()}')

def event_falling(pin):
    print(f'event_falling: PIN: {pin}, VALUE: {pin.value()}')

pin = Pin(0, Pin.IN)  # GPIO0に対して、入力を設定
pin.irq(trigger=Pin.IRQ_RISING, handler=event_rising)
pin.irq(trigger=Pin.IRQ_FALLING, handler=event_falling)

while True:
    time.sleep(1)
 
```

event_fallingしか動いていないことが分かると思います。イベントハンドラは上書きされて、event_risingは呼ばれなくなります。

[トップへ戻る](../README.md)
