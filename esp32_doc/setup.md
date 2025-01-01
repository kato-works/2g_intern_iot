# 開発環境のセットアップとESP32へのファームウエアの書き込み

## ツール・ファームなど

シリアルドライバイアは、接続した際にCOMポートに表示がされない場合にインストールしてください。（WindosではCOM、Macでは/dev/tty.*を確認）

- [Thonny](https://thonny.org/) Python IDE for beginners
- [FirmWare](https://micropython.org/download/ESP32_GENERIC/) ESP32 MicroPython FirmWare
- [CH340 Serial Driver](CH341SER.zip) シリアル接続ドライバ

> [!WARNING]
> シリアルドライバは、開発ボードの実装メーカーによって異なるので要注意です。オフィシャルサイトにも別のドライバのリンクが張られているので、マウントできなければこちらを試してください。
> 
> [Establish Serial Connection with ESP32](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/establish-serial-connection.html)

## PCとの接続（ドライバのインストール）

1. ESP32のFirmwareをダウンロード
   - [FirmWare](https://micropython.org/download/ESP32_GENERIC/) ESP32 MicroPython FirmWare
   - 本実習ではESP32_GENERIC-20240602-v1.23.0.binで動作確認を行っています
   - <image src="../images/download_firmware.png" width="400px">
1. ESP32をPCにUSBケーブルで接続
1. Windowsの「デバイスマネージャ」を起動し「ポート(COMとLPT)」に「USB-SERIAL CH340 (COMXX) 」と表示されていることを確認
   - COMXXは各自で異なるので、メモしてください
   - <image src="../images/device_manager.png" width="400px">
1. USB-SERIALの表示がない場合には、CH340のドライバをインストールして再接続
   - [CH340 Serial Driver](CH341SER.zip) シリアル接続ドライバ

> [!CAUTION]
> ESP32のUSBコネクタは強くないので、折らないように気を付けてください。

## ファームウェアの書き込み

1. Thonnyをダウンロードし、PCにインストール
   - <image src="../images/thonny_00.png" width="350px">
   - <image src="../images/thonny_install.png" width="350px">
1. Thonnyを起動して、上部メニューの "Tools" - "Options" を選択
   - <image src="../images/thonny_01.png" width="350px">
1. "Thonny Options"画面の、"Interpreter"のタブを開く
   - <image src="../images/thonny_02.png" width="350px">
1. "Which kind of interpreter"から "MicroPython(ESP32)"を選択、"Port WebREPL"から、先ほどメモしたCOMの番号を選択
   - <image src="../images/thonny_03.png" width="350px">
   - <image src="../images/thonny_04.png" width="350px">
1. 「Install or Update MicroPython (esptool)」のリンクを選択
   - <image src="../images/thonny_05.png" width="350px">
1. 「Install MicroPython (esptool)」のTarget portから、先ほどメモしたCOMの番号を選択
   - <image src="../images/thonny_06.png" width="350px">
1. 下部のメニューボタン"≡"から"Select local MicroPython image"を選択し、先ほどダウンロードしたFirmwareを選択する。
   - <image src="../images/thonny_07.png" width="350px">
1. "Install"ボタンを押すと、ファームウェアの書き込みがはじまる
   - <image src="../images/thonny_08.png" width="350px">
   - <image src="../images/thonny_09.png" width="350px">
1. 書き込みが完了したら、"Close"を押して"Install or Update MicroPython (esptool)"画面を閉じる
   - <image src="../images/thonny_10.png" width="350px">
1. 「Thonny Options」画面の「OK」を押してオプション画面を閉じる
   - <image src="../images/thonny_11.png" width="350px">
1. Thonnyの画面下部のShellに">>>"と表示されることを確認する。
   - <image src="../images/thonny_12.png" width="350px">


## プログラム実行の確認

1. Thonnyの上部の入力欄に、print('Hello')と入力し「F5」ボタンまたは緑の「Run」ボタンを押下
   - <image src="../images/thonny_13.png" width="350px">
1. 下部の出力に"Hello"と表示されることを確認
   - <image src="../images/thonny_14.png" width="350px">

[トップへ戻る](../README.md)
