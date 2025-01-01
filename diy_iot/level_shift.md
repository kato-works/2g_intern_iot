# 昇圧（レベルシフト）の仕方

5Vのでデジタル入力に対して、3.3Vを入力することでONにすることは出来ますが、安定度が低くなります。

以下のような回路を組むことで5Vで入力することが出来ます。

```scss
                    +5V
                      |
                     Collector
                      |
ESP32 GPIO (3.3V) ----|<| Base of PNP Transistor (e.g., 2N2907)
                      | 
                    Emitter
                      |
                      Load (e.g., LED, another circuit) ----> GND
```
