import time

running = True  # 実行中フラグ


def print_messages(messages, sleep_time_ms):
    """
    指定されたメッセージの配列を、指定されたスリープ間隔で順に表示し、
    KeyboardInterruptで中断されるか、runnningがFalseに設定されるまで繰り返す。

    Parameters
    ----------
    messages : str[]
        表示する文字列の配列
    sleep_time_ms : int
        表示間隔（ミリ秒）
    """
    try:
        while running:
            for message in messages:  # 指定された配列のメッセージを繰り返す
                print(message)
                time.sleep_ms(sleep_time_ms)  # 指定ミリ時間、一時停止する

    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
    
    return


if __name__ == "__main__":
    SLEEP_TIME_MS = 1000
    print_messages(
        messages=['Hello', 'World'],
        sleep_time_ms=SLEEP_TIME_MS,
    )
