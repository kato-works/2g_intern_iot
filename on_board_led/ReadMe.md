# IoT練習: 02.オンボードのLEDを光らせてみよう

## 本練習の目的

- GPIOの出力を経験する
- タイマーや繰り返しを使いこなす

## 実装内容

仕様：１秒間隔で、オンボードのLED（赤の電源LEDではなく、青のLED）を点滅させる

ESP32では32本のピンを持ち、プログラムから各ピンの機能・入出力を設定することができます。 GPIOを入力の場合にはON/OFFの読み出しを、出力の場合にはON/OFFの書き込みと読み出しができます。

各ピンからセンサの状態を入力として読み込んだり、出力から周辺のデバイスを操作したりすることで、制御を実現します。

- オンボードのLEDのピンは"2"です。

> [!NOTE]
> ON/OFFとはピンにかかっている電圧のことで、2.475Vから3.6Vが測定されるとON、-0.3Vから0.825Vが測定されるとOFFと判断されます。

## 以下を実行して結果を確認してみましょう

点灯する

```python
from machine import Pin

# GPIO2に接続された内蔵LEDを制御するためのPinオブジェクトを作成
# 2番のピンを、出力（Pin.OUT）に設定する。
led = Pin(2, Pin.OUT)
led.on()  # LEDを点灯
```

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(1)  # LEDを点灯

print(f'LED:{led.value()}')  # 現在のピンの状態を取得して表示
```

消灯する

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.off()  # LEDを消灯
```

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(0)  # LEDを消灯

print(f'LED:{led.value()}')
```

> [!NOTE]
> プログラムが終了してもGPIOのON/OFF状態（電位）は維持されるので、OFFに設定するか電源を切らないと点灯したままになります。

[トップへ戻る](../README.md)
