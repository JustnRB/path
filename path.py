import time #imports time library needed to run the code
import board #imports board library needed to run the code
import digitalio #imports digitalio library needed to run the code
import pwmio #imports pwnio library needed to run the code

from adafruit_motor import motor #imports small section of the adafruit_motor library

left_motor_forward = board.GP15 #initializes the variable left_motor_forward and attaches it to gp12
left_motor_backword = board.GP14 #initializes the variable right_motor_forward and attaches it to gp13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #tells pico this is an output
pwm_Lb = pwmio.PWMOut(left_motor_backword, frequency=10000) #tells pico this is an output

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #configuraton line and its required
Left_Motor_speed = 0 #initilizes the variable left_motor_speed to 0

right_motor_forward = board.GP13#initializes the variable right_motor_forward and attaches it to gp14
right_motor_backword = board.GP12#initializes the variable right_motor_forward and attaches it to gp15

pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000)#tells pico this is an output
pwm_Lb = pwmio.PWMOut(right_motor_backword, frequency=10000)#tells pico this is an output

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb) #configuraton line and its required
Right_Motor_speed = 0 #initilizes the variable right_motor_speed to 0

def forward():
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
def backward():
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
def left():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
def right():
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
while True:
    forward()
    time.sleep(1)
    backward()
    time.sleep(1)
    left()
    time.sleep(1)
    right()
    time.sleep(1)

# Write your code here :-)
