import time
import board
import busio
import adafruit_mpu6050
import math

# 构建I2C对象，使用核桃派I2C1控制
i2c = busio.I2C(board.SCL1, board.SDA1)

# 构建MPU6050对象
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    # 获取加速度计数据
    acceleration = mpu.acceleration

    # 获取陀螺仪数据
    gyro = mpu.gyro

    # 计算pitch, roll, yaw
    pitch = math.atan2(acceleration[0], math.sqrt(acceleration[1]**2 + acceleration[2]**2))
    roll = math.atan2(acceleration[1], math.sqrt(acceleration[0]**2 + acceleration[2]**2))
    yaw = math.atan2(math.sqrt(acceleration[0]**2 + acceleration[1]**2), acceleration[2])

    # 将弧度转换为角度
    pitch = math.degrees(pitch)
    roll = math.degrees(roll)
    yaw = math.degrees(yaw)

    # 打印数据
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % acceleration)
    print("Gyro: X:%.2f, Y: %.2f, Z: %.2f rad/s" % gyro)
    print("Pitch: %.2f degrees" % pitch)
    print("Roll: %.2f degrees" % roll)
    print("Yaw: %.2f degrees" % yaw)
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)