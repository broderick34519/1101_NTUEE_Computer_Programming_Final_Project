import RPi.GPIO as gpio
import time 


def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(19, gpio.OUT)
    gpio.setup(26, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(20, gpio.OUT)
    
def go_in(sec):
    init()
    gpio.output(19, False)
    gpio.output(26, True)
    gpio.output(16, True)
    gpio.output(20, False)
    time.sleep(sec)
    gpio.cleanup()
    
def go_out(sec):
    init()
    gpio.output(19, True)
    gpio.output(26, False)
    gpio.output(16, False)
    gpio.output(20, True)
    time.sleep(sec)
    gpio.cleanup()
   
last_file_time = ''

time_const = 2 # (sec)

def main():
	go_out(time_const)
	go_in(time_const)
