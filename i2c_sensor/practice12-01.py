from machine import Pin, I2C
import time

PIN_SCL = 22
PIN_SDA = 21

class AHT20:
    """
    AHT20測定クラス
    """

    def __init__(self, i2c):
        """
        コンストラクタ

        Parameters:
        -----------
        i2c : I2Cオブジェクト
        """
        self.i2c = i2c
        self.addr = 0x38
        self._init_sensor()

    def _init_sensor(self):
        """
        センサーの初期化(コマンド"\xBE"の送信)
        """
        self.i2c.writeto(self.addr, b'\xBE')
        time.sleep(0.02)

    def _read_data(self):
        """
        測定・データの読み込み（測定コマンドの送信）
        """
        self.i2c.writeto(self.addr, b'\xAC\x33\x00')
        time.sleep(0.08)
        data = self.i2c.readfrom(self.addr, 6)
        return data

    def get_temperature_humidity(self):
        """
        温度・湿度の読み込み
        """
        data = self._read_data()
        humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) / (1 << 20) * 100
        temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) / (1 << 20) * 200 - 50
        return temperature, humidity

def main():
    
    i2c = I2C(0, scl=Pin(PIN_SCL), sda=Pin(PIN_SDA), freq=400000)
    sensor = AHT20(i2c)

    while True:
        temperature, humidity = sensor.get_temperature_humidity()
        print("Temperature: {:.2f} C, Humidity: {:.2f} %".format(temperature, humidity))
        time.sleep(1)

if __name__ == '__main__':
    main()
