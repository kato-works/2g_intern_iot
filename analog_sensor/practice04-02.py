import time
import esp32


def fahrenheit_to_celsius(temperature_fahrenheit):
    """
    華氏を摂氏に変換する

    Parameters
    ----------
    temperature_fahrenheit : int
        華氏
    """
    temperature_celsius = (temperature_fahrenheit - 32) * 5.0 / 9.0
    return int(temperature_celsius)


def read_temperature(sleep_time_ms, is_celsius=True):
    """
    指定されたスリープ間隔でオンボードの温度を読み込み摂氏で表示する、
    中断されるまで繰り返す。

    Parameters
    ----------
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    is_celsius : bool
        摂氏での表示はTrue、華氏の表示はFalseを指定
    """
    try:
        while True:
            temperature_fahrenheit = esp32.raw_temperature() # MCUの内部温度を華氏で読み取る
            if is_celsius:
                temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
                print(f'temperature_celsius: {temperature_celsius} ℃')
            else:
                print(f'temperature_fahrenheit: {temperature_fahrenheit} ℉')

            time.sleep_ms(sleep_time_ms)
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
    
    return


if __name__ == "__main__":
    SLEEP_TIME_MS = 1000
    read_temperature(
        sleep_time_ms=SLEEP_TIME_MS,
        is_celsius=True,
    )
