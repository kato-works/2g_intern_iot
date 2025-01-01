# IoT練習: 13.センサーキットから好きなセンサーを選んで、デバイスを設計・試作しよう

## 本練習の目的

- 自分で機能・仕様を考えられるようになる
- 設計～試作まで自力で進められるようになる

## 注意！

ESP32のGPIOは3.3Vが上限値となるので、5Vのセンサーからデジタル・アナログ入力を受ける場合には、分圧回路を通してあげる必要があります。(ESP32は丈夫ですが、壊れるおそれがあります。)

<image src="bunnatsu_kairo.png">

```text
Vout = 3.3
Vin = 5.0
Vout = Vin * R2 / (R1 + R2)

3.3 = 5.0 * R2 / (R1 + R2)
R1 = (1.7 / 3.3) * R2
   = 0.52 * R2
```

5Vセンサーのアナログ出力を、5.0Vから3.3Vに降圧して32番ピンに入力する例

<image src="practice13.png" width="500px">

## 実装内容

いままでの練習内容を加味して、IoTデバイスを設計・開発してください。
仕様は自分で決めてみましょう。

- 入力はなにか？
  - センサー
  - ボタン
- 出力はなにか？
  - 標準出力（print）
  - LED
  - インターネットへ送信
  - ブザー
- 入力をどのように処理して、出力するか？
  - 何を条件分岐とするか
  - 条件に抜け漏れはないか
- どのPINを何に利用するのか、リストアップしよう

利用する部品の個々の動作を確認しよう。

- 期待した入力が得られるか？
- 期待した通りの出力が得られるか？
- 再利用できるように、関数にしておこう。

どのように組み合わせて、プログラムを作成するか？

## センサー例

以下のようなセンサーを準備しました。ほかにもESP32が備える機能を活用しても良いでしょう。

- 入力センサー
  - ボタン
  - 衝突検知
  - ライントレース
  - 赤外線障害物検知
  - 磁気検知
  - 振動検知
  - 傾き検知
  - タッチ検知
  - 人感センサー
  - 温度計
  - 光センサー
  - 音量センサー
  - アルコールセンサー
  - 明度センサー
  - 赤外線受信
  - 心拍計
  - ジョイスティック
  - 回転検出
  - 温度・湿度センサー
- 出力センサー
  - 各種LED
    - 白
    - RGBで色が調整かのうなもの
    - 明るいもの
    - 3色せっとのもの
  - ブザー
    - デジタル単音
    - PWMで音色が変えられるもの
  - 赤外線送信

## センサー一覧

詳細はこちらの [PDF](KS0349 Keyestudio 48 in 1 Sensor Kit.pdf) を参照

- 1: White LED Module
  - 白色LED（ON/OFF制御）
  - PIN
    - S(DI): ON/OFF
    - +: 5V
    - -: GND
  - 抵抗がすでに入っているので、挟む必要はありません
- 2: RGB LED Module
  - フルカラーLED（アナログ3ch）
  - PIN
    - G(AI): Analog Green
    - R(AI): Analog Red
    - B(AI): Analog Blue
    - G: Ground
  - 5V用のLEDなので3.3Vだと少し暗いかも
  - 残念ながらESP32はアナログ2chまでなのでフルカラーにはなりません。
  - PWMを用いるか、さらにローパスフィルターを設定する必要があります（PWNでここは十分）
  - 抵抗がすでに入っているので、挟む必要はありません
- 3: 3W LED Module
  - 明るいLED
  - PIN
    - S(DI): ON/OFF
    - +: 3.3V / 5V
    - -: GND
  - 抵抗がすでに入っているので、挟む必要はありません
- 4: Traffic Light Module
  - ３色表示LED
  - PIN
    - R(DI): Red
    - Y(DI): Yellow
    - G(DI): Green
    - GND: GND
  - 抵抗がすでに入っているので、挟む必要はありません
- 5: Active Buzzer Module
  - アクティブブザー
  - PIN
    - S(DI): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 6: Passive Buzzer Module
  - パッシブブザー
  - PIN
    - S(PWM IN): ON/OFF
    - +: 3.3V / 5V
    - -: GND
  - machine.PWMを使うことで、音色を指定して音を鳴らせます。
- 7: Digital Push Button Module
  - デジタルボタン
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 8: Collision Sensor
  - 衝突センサー（実質ボタン？）
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 9: Line Tracing Sensor
  - ライントレースセンサー
  - PIN
    - S(DO): ON/OFF
    - +: 5V
    - -: GND
  - 白い背景に黒い線・黒い背景に白い線を判定
- 10: Infrared Obstacle Avoidance Sensor
  - 赤外線障害物センサ
  - PIN
    - EN: リセットなので接続しない
    - S(DO): 障害物の検出
    - V: 3.3V / 5V
    - G: GND
- 11: Photo Interrupter Module
  - フォトインタラプタ
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
  - センサの隙間にモノがあるかどうか判定
- 12: Hall Magnetic Sensor
  - 磁気センサ
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 13: Knock Sensor Module
  - 振動センサー
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 14: Ditital Tilt Sensor
  - 傾きセンサー
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
  - 角度がわかるわけではありません。
- 15: Capacitive Touch Sensor
  - タッチセンサー
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 16: Flame Sensor
  - 炎（特定周波数の光）センサー
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 17: Reed Switch Module
  - リードスイッチ（磁気スイッチ）
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 18: PIR Motion Sensor
  - 人感センサー
  - PIN
    - S(DO): ON/OFF
    - +: 3.3V / 5V
    - -: GND
  - 今までの実習課題で使ったものと同じセンサーです
- 19: Analog Temperature Sensor
  - アナログ温度計
  - PIN
    - S(AO): NTCサーミスタ（温度センサー）の抵抗値
    - +: 5V
    - -: GND
  - ESP32のアナログ信号は0~3.9Vなので、注意が必要
  - エンコードを行う関数をちゃんと作ってみる
- 20: Analog Rotation Sensor
  - アナログ回転センサー
  - PIN
    - S(AO): 角度
    - +: 3.3V / 5V
    - -: GND
- 21: Photocell Sensor
  - 光センサー
  - PIN
    - S(AO): 明るさ
    - +: 5V
    - -: GND
- 22: Analog Sound Sensor
  - 音量センサー
  - PIN
    - S(AO): 音量
    - +: 3.3V / 5V
    - -: GND
- 23: Water Sensor
  - 水位センサー
  - PIN
    - S(AO): 水位
    - +: 5V
    - -: GND
- 24: Soil Humidity Sensor
  - 土中湿度センサー
  - PIN
    - S(AO): 湿度
    - +: 3.3V / 5V
    - -: GND
- 25: Analog Gas Sensor
  - ガス検知センサー（MQ2）
  - PIN
    - S(AO): ガス濃度
    - +: 5V
    - -: GND
- 26: Analog Alcohol Sensor
  - アルコール検知センサー（MQ3）
  - PIN
    - S(AO): アルコール濃度
    - +: 5V
    - -: GND
- 27: Steam Sensor
  - 蒸気センサー
  - PIN
    - S(AO): 蒸気濃度
    - +: 5V
    - -: GND
- 28: Analog Piezoelectric Ceramic Vibration Sensor
  - アナログ振動センサー
  - PIN
    - S(AO): 振動量
    - NC: 3.3V / 5V
    - -: GND
- 29: Voltage Sensor
  - 電圧センサー
  - PIN
    - S(AO): 0V ~ 25V
    - NC: 5V
    - -: GND
- 30: Tin-film Pressure Sensor
  - 圧力センサー
  - PIN
    - S(AO): 0 ~ 10Kg
    - +: 3.3V / 5V
    - -: GND
- 31: TEMT6000 Ambient Light Sensor
  - 明度センサー
  - PIN
    - S(AO): 明るさ
    - +: 5V
    - -: GND
- 32: DUVA-S12SD 3528 Ultraviolet Sensor
  - 紫外線センサー
  - PIN
    - S(AO): 明るさ
    - +: 2.5V ~ 5V
    - -: GND
- 33: Digital IR Receiver Module
  - 赤外線受信機
  - PIN
    - S(DO): ON/OFF
    - +: 5V
    - -: GND
- 34: Digital IR Transmitter Module
  - 赤外線送信機
  - PIN
    - S(DI): ON/OFF
    - +: 3.3V / 5V
    - -: GND
- 35: Pulse Rate Monitor Module
  - 心拍計
  - PIN
    - S(AO): 心拍数
    - +: 5V
    - -: GND
- 36: Joystic Module
  - ジョイスティック
  - PIN
    - X(AO): X軸
    - Y(AO): Y軸
    - Z(DO): Z軸
    - +: 3.3V / 5V
    - -: GND
- 37: Rotary Encoder Module
  - ロータリーエンコーダー(回転検出)
  - PIN
    - CIK(DO): クロック信号（回転すると0/1を繰り返す）
    - DT(DO): データ信号（CLKと90度ずれるため、回転方向の検出に用いる）
    - SW(DO): スイッチ信号
    - +: 5V
    - -: GND
- 38: 5V 1 Channel Relay Module
  - リレー（回路開閉スイッチ）
  - PIN
    - S(DI): 開閉指示
    - +: 5V
    - -: GND
- 39: LM35 Linear Temperature Sensor
  - 温度センサー
  - PIN
    - S(AO): 0 ~ 100℃ (10mV/℃)
    - +: 5V
    - -: GND
  - 3.3Vに降圧して利用した場合には以下の計算式（そのまま直結した場合には500.0）
    - adc.read() * 330.0 / 1023
- 40: DHT11 Temperature and Humidity Sensor
  - 温度・湿度センサー
  - PIN
    - S(Serial TX): 9600bpsで5byteのデータを送信
      - 第1バイト（8ビット）：湿度の整数部分
      - 第2バイト（8ビット）：湿度の小数部分（DHT11では常に0）
      - 第3バイト（8ビット）：温度の整数部分
      - 第4バイト（8ビット）：温度の小数部分（DHT11では常に0）
      - 第5バイト（8ビット）：チェックサム（第1～第4バイトの合計の下位8ビット）
    - +: 5V
    - -: GND
- 41: Magical Light Cup Module
  - よくわからない、明るさ調整できるセンサー？？
  - PIN
    - L(DI): LED
    - S(DO): BUTTON
    - +: 3.3V / 5.0V
    - -: GND
- 42: APDS-9930 Attitude Sensor Module
  - 周囲光センサー
  - PIN
    - 3.3V: 3.3V
    - GND: GND
    - SDA: I2C Data
    - SCL: I2C Clock
    - INT: Interrupt
- 43: ALS Infrared LED Optical Proximity Detection Module
  - 環境光、近接センサー、赤外線LEDの複合センサー
  - PIN
    - 3.3V: 3.3V
    - GND: GND
    - SDA: I2C Data
    - SCL: I2C Clock
    - INT: Interrupt
- 44: MMA8452Q Triaxial Digital Acceleration Tilt Sensor
  - 3軸加速度センサー
  - PIN
    - 3.3V: 3.3V
    - GND: GND
    - SDA: I2C Data
    - SCL: I2C Clock
    - INT: Interrupt
- 45: 9G Servo Motor
  - PWMサーボモーター
  - PIN
    - オレンジ(DI): 
    - 赤: 5V
    - 茶: GND
- 46: HC-SR04 Blue Ultrasonic Sensor
  - 超音波センサー（距離測定）
  - PIN
    - VCC: 5V
    - Trig(DI): 発信指示
    - Echo(DO): 受信検知
    - GND: GND
  - machine.time_pulse_usを使うと応答時間が計測できます。
- 47: Keystudio 0820 LCD module 5V blue screen
  - LCDスクリーン
- 48: Keystudio 8x8 LED Matrix Module Address Select
  - 8x8ドットマトリックス
  - PIN
    - 3.3V: 3.3V
    - GND: GND
    - SDA: I2C Data
    - SCL: I2C Clock
    - INT: Interrupt
