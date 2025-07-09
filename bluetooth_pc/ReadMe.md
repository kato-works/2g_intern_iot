# IoT練習: 13.BluetoothでPCと通信してみよう

## 本練習の目的

- ESP32のBluetooth(BLE)機能を使ってみる
- PCとデータを送受信する方法を知る
- サービスとキャラクタリスティックの概念を理解する

## 実装内容

仕様: ESP32をBLE周辺機器として起動し、PCから接続して文字列を送受信しよう

ここではNordic UART Service(NUS)と呼ばれるシリアル通信に近い方式を利用します。

## 以下を実行して結果を確認してみましょう

ESP32側の例

```python
import bluetooth
import time

_UART_SERVICE_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_RX = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_TX = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

_IRQ_CENTRAL_CONNECT = 1
_IRQ_CENTRAL_DISCONNECT = 2
_IRQ_GATTS_WRITE = 3

ble = bluetooth.BLE()
ble.active(True)


def bt_irq(event, data):
    if event == _IRQ_CENTRAL_CONNECT:
        print("PC connected")
    elif event == _IRQ_CENTRAL_DISCONNECT:
        print("PC disconnected")
    elif event == _IRQ_GATTS_WRITE:
        conn_handle, value_handle = data
        value = ble.gatts_read(value_handle)
        print("RX:", value)

ble.irq(bt_irq)

# サービスとキャラクタリスティックの登録
UART_SERVICE = (
    _UART_SERVICE_UUID,
    (
        (_UART_TX, bluetooth.FLAG_NOTIFY,),
        (_UART_RX, bluetooth.FLAG_WRITE,),
    ),
)
((tx_handle, rx_handle),) = ble.gatts_register_services((UART_SERVICE,))

name = b'mpy-ble'
adv = b"\x02\x01\x06" + bytes((len(name) + 1, 0x09)) + name
ble.gap_advertise(100, adv)

while True:
    ble.gatts_notify(0, tx_handle, b"Hello PC")
    time.sleep(5)
```

PC側ではPythonの`bleak`ライブラリを使うと簡単に接続できます。

```sh
pip install bleak
```

```python
import asyncio
from bleak import BleakClient

ADDRESS = "xx:xx:xx:xx:xx:xx"  # デバイスアドレス
UART_SERVICE = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

async def main():
    async with BleakClient(ADDRESS) as client:
        await client.start_notify(UART_TX, lambda h, data: print(data.decode()))
        await client.write_gatt_char(UART_RX, b"Ping")
        await asyncio.sleep(10)

asyncio.run(main())
```

[トップへ戻る](../README.md)
