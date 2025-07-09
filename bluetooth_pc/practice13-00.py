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
