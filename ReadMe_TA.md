# 講師準備編

2024年度実施インターンの準備をまとめて、以降に講師になる人がいた場合のためのメモ

## 準備物

- ESP-WROOM-32
  - ESP32の30PinでType-Cインタフェースのもの、時々オンボードのLEDがないタイプがあるので注意
- SAD-101
  - サンハヤトの6穴ブレッドボード、5穴のボードの場合にはESP32が幅広なので2枚連結させる必要がある。
  - https://shop.sunhayato.co.jp/products/sad-101
- PIR AM312
  - ミニ赤外線赤外線 モーションセンサー
- LED
- 抵抗200Ω程度
- ジャンパー線（オスオス、オスメス）
- USBケーブル（データ通信対応のもの）

## ストレッチ課題用センサー

- KEYESTUDIO センサーアソートキット センサモジュール スターター キット(keyestudio 48 in 1 sensor kit)
  - https://wiki.keyestudio.com/KS0349_Keyestudio_48_in_1_Sensor_Kit
  - https://www.amazon.co.jp/gp/product/B0CQJBQ4Y3
- 分圧回路のための抵抗 1KΩ / 2KΩ
  - 分圧回路 : https://www.kairo-nyumon.com/resistor_divider.html

## 開発環境など

- Thonny : MicroPython開発環境（ファーム書き込みツール付）
  - https://thonny.org/ 
- Fritzing : ブレッドボード回路図作成ツール
  - 有償版 https://fritzing.org/
  - OSS版 https://github.com/fritzing/fritzing-app/releases/tag/CD-548
  - 今回の実習の部品 [.fzpzファイル](images/fritzing)
 
## その他参照サイト

- ESP32 メーカーサイト
  - https://www.espressif.com/en/products/devkits/esp32-devkitc
- ESP32 Micropython リファレンス
  - 英語 : https://docs.micropython.org/en/latest/esp32/quickref.html
  - 日本語(ちょっと情報が古い) : https://micropython-docs-ja.readthedocs.io/ja/latest/esp32/quickref.html
- SORACOM IoT DIY レシピ : ESP32に限らずIoTのDIY事例集
  - https://soracom.jp/iot-recipes/
- Pythonの基礎学習
  - https://paiza.jp/works/python/trial
  - プログラミングとは
    - コンピュータを制御するプログラムをつくること
    - ソースコード：プログラムの記述内容
    - プログラミング言語：ソースコードを記述する専用言語
  - はじめてのプログラミング
    - print('Hello World')
  - 間違いやすいポイント
    - エラーを出してみる
    - 全角半角・大文字小文字
  - 数値を扱う
  - プログラムで計算する
  - 変数にデータを入れる
  - データを受け取る
  - 標準入力と標準出力
  - 条件に一致したら処理を実行する
  - 条件に合わせて処理を変える
  - 数値を分類する
  - 同じ処理を何度も繰り返す
  - 複数のデータを受け取る
  - 複数データを分類する

https://github.com/targetblank/micropython_ahtx0/blob/master/ahtx0.py

## 追加で購入したセンサー

- AHT20 温度・湿度センサー
  - I2Cを介して温度と湿度のデータを取得出来るセンサー
  - データレイアウト
    - 0: 0x00 (常に0)
    - 1: Status (ステータス)
    - 2: Humidity MSB (湿度上位バイト)
    - 3: Humidity LSB (湿度中位バイト)
    - 4: Humidity/Temperature Mixed (湿度下位/温度上位バイト)
    - 5: Temperature MSB (温度上位バイト)
    - 6: Temperature LSB (温度下位バイト)
  - コマンド
    - 初期化コマンド : 0xBE
      - センサーをリセットし、初期化
    - 測定開始コマンド : 0xAC 0x33 0x00
      - 測定を開始
- 振動センサー
  - PIN
    - S(AO): 振動量
    - +: 3.3V / 5V
    - -: GND
- コンデンサーマイク（LM393）
  - PIN
    - AO(AO): マイクのリアルタイム電圧信号
    - G: GND
    - +: 3.3V / 5V
    - DO(DO): 音の強度がしきい値に達すると、信号を出力
