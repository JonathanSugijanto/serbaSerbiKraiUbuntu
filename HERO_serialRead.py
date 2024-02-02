import serial 
import time 

# def print_serial(name):
#     try:
#         serial_port = serial.Serial(name,115200)
#         print(f"The Port name is {serial_port.name}")
#     except:
#         print("ERROR")
#         print("check port")
#         exit() 

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1) 
def write_read(x): 
    # arduino.write(bytes(x, 'utf-8')) 
    # time.sleep(0.05) 
    data = arduino.readline() 
    return data 
while True: 
    # num = input("Enter a number: ") # Taking input from user 
    value = arduino.readline() 
    print(value) # printing the value 
    # time.sleep(0.1)
