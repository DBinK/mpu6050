import time
import board
import busio
import adafruit_mpu6050
import math

# 构建I2C对象，使用核桃派I2C1控制
i2c = busio.I2C(board.SCL1, board.SDA1)

# 构建MPU6050对象
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

# 初始化互补滤波参数
alpha = 0.98  # 加速度计权重
dt = 0.01  # 采样间隔

# 初始化姿态角度
pitch = 0
roll = 0
yaw = 0

# 循环读取数据并进行校正
while True:
    # 获取加速度计数据
    acceleration = mpu.acceleration

    # 获取陀螺仪数据
    gyro = mpu.gyro

    # 计算加速度计的pitch、roll和yaw角度
    pitch_acc = math.atan2(acceleration[0], math.sqrt(acceleration[1]**2 + acceleration[2]**2))
    roll_acc = math.atan2(acceleration[1], math.sqrt(acceleration[0]**2 + acceleration[2]**2))
    yaw_gyro = gyro[2] * dt

    # 使用互补滤波算法进行校正
    pitch = alpha * (pitch + gyro[0] * dt) + (1 - alpha) * pitch_acc
    roll = alpha * (roll + gyro[1] * dt) + (1 - alpha) * roll_acc
    yaw += yaw_gyro
    
    # 使用互补滤波算法对yaw角度进行融合
    #yaw = alpha * (yaw + yaw_gyro) + (1 - alpha) * yaw_acc

    # 将弧度转换为角度
    pitch_deg = math.degrees(pitch)
    roll_deg = math.degrees(roll)
    yaw_deg = math.degrees(yaw)

    # 打印数据
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % acceleration)
    print("Gyro: X:%.2f, Y: %.2f, Z: %.2f rad/s" % gyro)
    print("Pitch: %.2f degrees" % pitch_deg)
    print("Roll: %.2f degrees" % roll_deg)
    print("Yaw: %.2f degrees" % yaw_deg)
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(dt)