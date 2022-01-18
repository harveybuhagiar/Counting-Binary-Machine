import machine
import utime


def auto_sequence(interval):
    global binary_1 
    global binary_2 
    global binary_3 
    global binary_4 
    global counter 
    
    while True:
        counter += 1
        utime.sleep(interval) #gap between incrementation
        if counter > 15:
            counter = 0  #reset counter to 0 after maximum value of 15
        print(counter)
    
        decimal_num = binary_conversion[counter] #array containing binary bits for corresponding decimal i.e. [0,0,1,1] = 3
        binary_4.value(decimal_num[0]) #turns lights on according to binary number
        binary_3.value(decimal_num[1])
        binary_2.value(decimal_num[2])
        binary_1.value(decimal_num[3])

def button_sequence():
    global binary_1 
    global binary_2 
    global binary_3 
    global binary_4 
    global counter 
    while True:
        if button.value() == 1: #if button pressed
            counter += 1
            utime.sleep(0.5) #time delay
            if counter > 15:
                counter = 0
            print(counter)
    
        decimal_num = binary_conversion[counter]
        binary_4.value(decimal_num[0])
        binary_3.value(decimal_num[1])
        binary_2.value(decimal_num[2])
        binary_1.value(decimal_num[3])

  
#APIs
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
binary_1 = machine.Pin(15, machine.Pin.OUT)
binary_2 = machine.Pin(13, machine.Pin.OUT)
binary_3 = machine.Pin(11, machine.Pin.OUT)
binary_4 = machine.Pin(12,machine.Pin.OUT)

counter = 0
binary_conversion = [[0,0,0,0],
                     [0,0,0,1],
                     [0,0,1,0],
                     [0,0,1,1],
                     [0,1,0,0],
                     [0,1,0,1],
                     [0,1,1,0],
                     [0,1,1,1],
                     [1,0,0,0],
                     [1,0,0,1],
                     [1,0,1,0],
                     [1,0,1,1],
                     [1,1,0,0],
                     [1,1,0,1],
                     [1,1,1,0],
                     [1,1,1,1]]

    

    


