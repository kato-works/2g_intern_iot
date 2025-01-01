from machine import Pin, I2C
import time

# I2Cのピン番号はハードウェアに依存しますが、通常は21と22です。
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

devices = i2c.scan()
if devices:
    for device in devices:
        print("I2C device found at address:", hex(device))
else:
    print("No I2C devices found")

MPU6050_I2C_ADDRESS = 0x68

PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
TEMP_OUT_H = 0x41
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
SIGNAL_PATH_RESET = 0x68
USER_CTRL = 0x6A

# MPU-6050を初期化する関数
def init_mpu6050():
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, PWR_MGMT_1, b'0x01')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, PWR_MGMT_2, b'0x00')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, SIGNAL_PATH_RESET, b'0x00')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, USER_CTRL, b'0x00')
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, SMPLRT_DIV, b'0x04')

init_mpu6050()
pwr_mgmt_2 = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, PWR_MGMT_2, 1)
print(pwr_mgmt_2)
