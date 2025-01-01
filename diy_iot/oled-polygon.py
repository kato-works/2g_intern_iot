# 3D points MicroPython version with ESP32 and ssd1306 OLED 

from machine import Pin, I2C
from micropython import const
from time import sleep_ms
from math import sin, cos, pi
from ssd1306 import SSD1306_I2C

# CUBE
"""
points = [
    [-20, -20, 20],
    [20, -20, 20],
    [20, 20, 20],
    [-20, 20, 20],
    [-20, -20, -20],
    [20, -20, -20],
    [20, 20, -20],
    [-20, 20, -20],
]

links = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7],
]
"""
"""
# AIRPLANE
points = [
    [-20, 0, 0],  # NOSE
    [20, 20, -5],
    [15, 0, 0],  # TAIL
    [20, -20, -5],
    [10, 0, -15],  # BOTTOM
]

links = [
    [0, 1], [0, 2], [0, 3], [0, 4],
    [1, 2], [2, 3],
    [2 ,4],
]
"""
# AIRPLANE2
points = [
    [0.0, 45.0, 0.0],  # NOSE
    [0.0, -45.0, 0.0],  # TAIL
    [5.18, -45.0, -19.32],  # TAIL R
    [-5.18, -45.0, -19.32],  # TAIL L
    [36.22, -51.88, -12.59], # WING R(TAIL)
    [-36.22, -51.88, -12.59], # WING L(TAIL)
    [42.02, -16.15, -2.81], # WING R(MID)
    [-42.02, -16.15, -2.81], # WING L(MID)
]

links = [
    [0, 1], [0, 2], [0,3], [0, 6], [0,7],
    [1, 2], [1, 3],
    [2, 4], [3, 5],
    [4, 6], [5, 7],
]

faces = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 4, 6],
    [0, 3, 5, 7],
]


# ESP32のI2Cピンを設定 (SCL=GPIO22, SDA=GPIO21)
X = const(64)
Y = const(32)
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(X * 2, Y * 2, i2c)

z_buffer = [[float('inf')] * (X * 2) for _ in range(Y * 2)]

f = []
for i in range(len(points)):
    f.append([0.0, 0.0, 0.0])

one_degree = pi / 180.0

def rotate(x, y, z, r):
    xr = x
    yr = y * cos(r) - z * sin(r)
    zr = y * sin(r) + z * cos(r)
    return xr, yr, zr

def normal(face):
    p0 = points[face[0]]
    p1 = points[face[1]]
    p2 = points[face[2]]
    
    u = [p1[i] - p0[i] for i in range(3)]
    v = [p2[i] - p0[i] for i in range(3)]
    
    n = [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ]
    
    return n

def is_visible(face):
    n = normal(face)
    return n[2] < 0


def draw_line_with_zbuffer(x0, y0, z0, x1, y1, z1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    dz = z1 - z0
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < X * 2 and 0 <= y0 < Y * 2:
            # 現在のZ値とバッファの値を比較
            if z0 < z_buffer[y0][x0]:
                z_buffer[y0][x0] = z0  # Zバッファの更新
                oled.pixel(x0, y0, 1)  # ピクセル描画
        
        if x0 == x1 and y0 == y1:
            break
        
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
        
        z0 += dz / max(dx, dy)  # Z値の更新

diff_roll = 6
diff_yaw = 6
diff_pitch = 6

angle_roll = 0
angle_yaw = 0
angle_pitch = 90

while True:
    angle_roll += diff_roll
    angle_yaw += diff_yaw
    angle_pitch += diff_pitch
    
    if angle_roll > 360:
        angle_roll -= 360
    
    if angle_yaw > 360:
        angle_yaw -= 360
        
    if angle_pitch > 360:
        angle_pitch -= 360
    
    for i in range(len(points)):
        r_roll  = angle_roll * one_degree  # 1 degree
        r_yaw  = angle_yaw * one_degree  # 1 degree
        r_pitch  = angle_pitch * one_degree  # 1 degree
        
        x0 = points[i][0]
        y0 = points[i][1]
        z0 = points[i][2]
        
        x1, y1, z1 = rotate(x0, y0, z0, r_roll)  # rotate X
        y2, z2, x2 = rotate(y1, z1, x1, r_yaw)  # rotate Y
        z3, x3, y3 = rotate(z2, x2, y2, r_pitch)  # rotate Z
        
        f[i][0] = x3 + X
        f[i][1] = y3 + Y
        f[i][2] = z3
    
    # Zバッファをクリア
    z_buffer = [[float('inf')] * (X * 2) for _ in range(Y * 2)]
    
    oled.fill(0)
    
    for face in faces:
        if is_visible(face):
            for i in range(len(face)):
                s = face[i]
                d = face[(i + 1) % len(face)]
                # print(s,d, f)
                draw_line_with_zbuffer(int(f[s][0]), int(f[s][1]), f[s][2], int(f[d][0]), int(f[d][1]), f[d][2])
    
    oled.text(f'{angle_roll:03},{angle_yaw:03},{angle_pitch:03}', 0, 0, 1)
    oled.show()  # display
    sleep_ms(1)

