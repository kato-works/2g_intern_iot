from machine import Pin, I2C
import time

# I2Cの初期化
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)

# I2Cスキャン
def scan_i2c():
    devices = i2c.scan()
    if devices:
        for device in devices:
            print("I2C device found at address:", hex(device))
    else:
        print("No I2C devices found")

scan_i2c()

# MPU-6050のアドレス
MPU6050_I2C_ADDRESS = 0x68  # 0x69の場合もあるので確認

# MPU-6050をリセット
def reset_mpu6050():
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x6B, b'\x80')  # リセットビットをセット
    time.sleep(1)  # リセット後に少し待機

# MPU-6050の初期化
def init_mpu6050():
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x6B, b'0x00')  # スリープ解除
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x6C, b'0x00')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x1B, b'0x00')  # ジャイロ範囲±250°/s
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x1C, b'0x00')  # 加速度範囲±2g
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x19, b'0x04')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x37, b'0x02')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, 0x38, b'0x01')

reset_mpu6050()
init_mpu6050()

# データのスケーリング
def scale_accel(raw_accel, fs_range=2):
    scale_factor = fs_range / 32768.0
    return raw_accel * scale_factor

def scale_gyro(raw_gyro, fs_range=250):
    scale_factor = fs_range / 32768.0
    return raw_gyro * scale_factor

# MPU-6050からデータを読み取る
def read_mpu6050():
    # 加速度データの読み取り（0x3Bから6バイト）
    accel_data = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, 0x3B, 6)
    # ジャイロデータの読み取り（0x43から6バイト）
    gyro_data = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, 0x43, 6)
    print(accel_data, gyro_data)
    
    # 加速度データの処理
    accel_x = int.from_bytes(accel_data[0:2], 'big')
    accel_y = int.from_bytes(accel_data[2:4], 'big')
    accel_z = int.from_bytes(accel_data[4:6], 'big')
    
    # ジャイロデータの処理
    gyro_x = int.from_bytes(gyro_data[0:2], 'big')
    gyro_y = int.from_bytes(gyro_data[2:4], 'big')
    gyro_z = int.from_bytes(gyro_data[4:6], 'big')
    
    # データのスケーリング
    accel_x = scale_accel(accel_x)
    accel_y = scale_accel(accel_y)
    accel_z = scale_accel(accel_z)
    
    gyro_x = scale_gyro(gyro_x)
    gyro_y = scale_gyro(gyro_y)
    gyro_z = scale_gyro(gyro_z)
    
    return (accel_x, accel_y, accel_z), (gyro_x, gyro_y, gyro_z)

# データの読み取りと表示
while True:
    accel, gyro = read_mpu6050()
    print("Accelerometer (g):", accel)
    print("Gyroscope (°/sec):", gyro)
    time.sleep(1)