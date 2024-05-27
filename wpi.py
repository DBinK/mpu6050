'''
实验名称：MPU6050六轴加速度计
实验平台：核桃派1B
'''
import time, board, busio, adafruit_mpu6050

# 构建I2C对象，使用核桃派I2C1控制
i2c = busio.I2C(board.SCL2, board.SDA2)

# 构建MPU6050对象
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    print("Acceleration: X = %.2f, Y = %.2f, Z = %.2f " % (mpu.acceleration))
    #print("Gyro: X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    #print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(0.1)