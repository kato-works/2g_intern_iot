from machine import Pin, I2C
import time

class AHT20:
    def __init__(self, i2c):
        self.i2c = i2c
        self.addr = 0x38
        self.init_sensor()

    def init_sensor(self):
        self.i2c.writeto(self.addr, b'\xBE')
        time.sleep(0.02)
        self.i2c.writeto(self.addr, b'\xAC\x33\x00')
        time.sleep(0.02)

    def read_data(self):
        self.i2c.writeto(self.addr, b'\xAC\x33\x00')
        time.sleep(0.08)
        data = self.i2c.readfrom(self.addr, 6)
        return data

    def get_temperature_humidity(self):
        data = self.read_data()
        humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) / (1 << 20) * 100
        temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) / (1 << 20) * 200 - 50
        return temperature, humidity

def main():
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
    sensor = AHT20(i2c)

    while True:
        temperature, humidity = sensor.get_temperature_humidity()
        print("Temperature: {:.2f} C, Humidity: {:.2f} %".format(temperature, humidity))
        time.sleep(1)

if __name__ == '__main__':
    main()
