import time
import esp32


def fahrenheit_to_celsius(temperature_fahrenheit):
    temperature_celsius = (temperature_fahrenheit - 32) * 5.0 / 9.0
    return int(temperature_celsius)


while True:
    temperature_fahrenheit = esp32.raw_temperature() # MCUの内部温度を華氏で読み取る
    temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
    print(f'temperature_celsius: {temperature_celsius} ℃')
    time.sleep(1)
