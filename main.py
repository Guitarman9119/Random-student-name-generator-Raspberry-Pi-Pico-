# Random name call out generator, thanks to reddit user onewaybackhome for inspiration to recreate this evil project
# on the raspberry pi pico. Also thanks for to Mike Causer for writing the max7219 library for micropython - https://github.com/mcauser/micropython-max7219
# There is room for improvement and will continue to do so in the future

import max7219 #library used              
from machine import Pin, SPI #from machine import Pin to setup button and SPI communication to max7219
from time import sleep #from time import sleep to control speed of text updated.
import random
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(5)     # adjust brightness 1 to 15



##------------Set up buttons-----------------------


button_random_student = Pin(14, Pin.IN, Pin.PULL_DOWN)  #button to random a student and display their name
button_select_class = Pin(15, Pin.IN, Pin.PULL_DOWN)    #button to go throught classes




#Change this code, so it will work for your class, add more classes to the dictionary along with the names:
classes = {}
classes['CS Class'] = ["Subscribe", "To", "Nerd", "Cave"]
classes['STEAM'] = ["Stefan", "Jack","Parow","Stan","Lee"]
classes['Science'] = ["random1","random2","random3","random4","random5"]
selected_class = 'Computer Science'
selected_class_index = 0



def display_function(msg):
    length = len(msg) # calculate the lenght of the msg / name / class
    length = (length*8)+1 # multiple by 8 and add one to calculate scroll lenght
    display.fill(0)
    display.show()
    sleep(0.5)
    for x in range(31, -length, -1):   #loop through the msg from right to left
        display.text(msg ,x,0,1)
        display.show()
        sleep(0.050)
        display.fill(0)
        
        
        
def countdown():
    counter = ["5","4","3","2","1"]
    lenght = len(counter)  #This will give a value of 5
    
    for i in range(0, lenght):
    
        number = counter[i] #set number to first item in counter list
        length = len(counter[i]) #calculate the lenght of counter
        length = (length*8) # times that by 8 to ensure it will scroll of screen
        display.fill(0)
        display.show()
        sleep(0.1) # delay before showing number
      

        for x in range(31, -lenght-1, -1): ##
            
            display.text(number ,x,0,1) #display the first number in list at right of screen and then scroll it from right to left
            display.show()
            sleep(0.03)  ##to controll the speed
            display.fill(0)
           
        



def get_bit(byteval,idx):
    return ((byteval&(1<<idx))!=0);

def displayImage(image): # list of ints as input
    for i, row in enumerate(image): # iterate through every row
        for j in range(0,32): # check all bits in row, and if bit is 1 send to LED display
            is_set = get_bit(row,j) # is bit j set inside byte string row
            if is_set:
                display.pixel(31-j,i,1) # display if position j is an on bit
    display.show() # display
            
    





#Make your own custom image to be displayed - This is a work in progress will make an
#easier solution in near future for now use: https://xantorohara.github.io/led-matrix-editor/
#It takes a bit of time to copy each byte in a 32 bit binary, should make a new web app to do this.
    
outer_img =  [0b11111111111111111111111111111111,
              0b10000000000000000000000000000001,
              0b10000000000000000000000000000001,
              0b10000000000000000000000000000001,
              0b10000000000000000000000000000001,
              0b10000000000000000000000000000001,
              0b10000000000000000000000000000001,
              0b11111111111111111111111111111111]

outer_img2 = [0b00000000000000000000000000000000,
              0b01111111111111111111111111111110,
              0b01000000000000000000000000000010,
              0b01000000000000000000000000000010,
              0b01000000000000000000000000000010,
              0b01000000000000000000000000000010,
              0b01111111111111111111111111111110,
              0b00000000000000000000000000000000]

outer_img3 = [0b00000000000000000000000000000000,
              0b00000000000000000000000000000000,
              0b00111111111111111111111111111100,
              0b00100000000000000000000000000100,
              0b00100000000000000000000000000100,
              0b00111111111111111111111111111100,
              0b00000000000000000000000000000000,
              0b00000000000000000000000000000000]

outer_img4 = [0b00000000000000000000000000000000,
              0b00000000000000000000000000000000,
              0b00000000000000000000000000000000,
              0b00011111111111111111111111111000,
              0b00011111111111111111111111111000,
              0b00000000000000000000000000000000,
              0b00000000000000000000000000000000,
              0b00000000000000000000000000000000]




while True:
    
    display.fill(0)
    displayImage(outer_img)
    sleep(0.5)
    display.fill(0)
    displayImage(outer_img2)
    sleep(0.5)
    display.fill(0)
    displayImage(outer_img3)
    sleep(0.5)
    display.fill(0)
    displayImage(outer_img4)
    sleep(0.5)
    display.fill(0)
    displayImage(outer_img3)
    sleep(0.5)
    display.fill(0)
    displayImage(outer_img2)
    sleep(0.5)   
    
    if button_random_student.value() == 1: #check if button state change from 0 to 1
        countdown() # call countdown function
        random_idx = random.randrange(0, len(classes[selected_class])) # create a random number depending on the number of students in the class
        random_student = classes[selected_class][random_idx] # select a random student from the selected class
        display_function(random_student) # display student name through the display_function function
        sleep(0.5)
    
    
    if button_select_class.value() == 1:  #check if button state change from 0 to 1
        selected_class_index = (selected_class_index + 1) % len(classes) #change index if button is pressed
        selected_class = list(classes.keys())[selected_class_index]  #assign new selected class through a list of the classes.keys()
        display_function(selected_class) # display selected class
        sleep(0.5)
        
  
   
     
 
        
   



    