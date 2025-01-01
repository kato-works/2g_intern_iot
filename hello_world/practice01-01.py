import time

messages = ['Hello', 'World']
SLEEP_TIME_MS = 1000

while True:
    for message in messages:  # 指定された配列のメッセージを繰り返す
        print(message)
        time.sleep_ms(SLEEP_TIME_MS)  # 指定ミリ時間、一時停止する
