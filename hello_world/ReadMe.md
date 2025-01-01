# IoT練習: 01.Hello Worldと表示してみよう

## 本練習の目的

- まずはESP32と触れ合ってみる
- MicroPythonの基本構文に慣れる

## 実装内容

仕様：１秒間隔で"Hello"と"World"を交互に表示する

プログラミングが初めての方は、サンプルを準備したので、自分のスキルに合わせて以下を学習しましょう。

- PRINT句の使い方
- 変数の使い方
- 条件分岐の方法
- スリープのさせかた
- ループ（WHILE句、FOR句）の使い方
- 関数の作り方・使い方

## 以下を実行して結果を確認してみましょう

■ PRINT句:　シリアルに文字を表示する

```python
print('Hello')
```

■ エラーを発生させてみよう

大文字小文字を間違えると、

```python
Print('Hello')
```

NameError: name 'Print' isn't defined と出るはずです。

では、'を閉じ忘れるとどう表示されるでしょう。

```python
print('Hello)
```

'の全角半角を間違えるとどう表示されるでしょう。

```python
print(’Hello’)
```

エラー表示は、なぜエラーになったかが記述されている大事な情報です。エラーをよく読んでソースコードを修正しましょう。

■ 変数: 値を入れたり取り出せたり出来る箱

```python
message = 'Hello'
print(message)

message = message + '!'
print(message)

count = 1
print(count + 5)
```

■ 条件分岐: プログラムに判定をさせる

```python
x = 5
y = 2

if x > y:
  print(f'x({x}) > y({y})')
elif x == y:  # 同じかどうかの判定は "==" で比較、"=" は代入の記号
  print(f'x({x}) = y({y})')
else:
  print(f'x({x}) < y({y})')
```

■ SLEEPの方法:　一定時間プログラム実行を停止する  

```python
import time  # ライブラリのインポート

print('Hello')
time.sleep(1)
print('Hello!')
time.sleep_ms(500)
print('Hello!!')
```

■ WHILE句(Ctl+Cでプログラム実行の中断): 終了条件を決めて処理をループする

```python
import time

while True:
  print('Hello')
  time.sleep(1)
```

■ FOR句: 実行回数を決めて処理をループする

```python
import time

for i in range(5):
  print(f'Hello:{i}')
  time.sleep(1)
```

■ 関数: 処理をまとめて、再利用可能にする仕組み

```python
def print_with_exclamation(message, count=3):
  print(message + '!' * count)

print_with_exclamation('Hello')
print_with_exclamation('Hello', 5)
```

[トップへ戻る](../README.md)
