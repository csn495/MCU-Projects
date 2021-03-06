#!/usr/bin/python3

'''
- Use with Raspberry pi.
- See README for requisites.
'''


from RPLCD import i2c
from time import sleep
import time
import board
import adafruit_mcp9808

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

#Beginning of my code

i2c = board.I2C()  # uses board.SCL and board.SDA

# To initialise using the default address:
mcp = adafruit_mcp9808.MCP9808(i2c,address=0x18)

# To initialise using a specified address:
# Necessary when, for example, connecting A0 to VDD to make address=0x19
# mcp = adafruit_mcp9808.MCP9808(i2c_bus, address=0x19)

while True:

    def read_temp():
        tempC = mcp.temperature
        temp = tempC * 9/5.0 + 32
#        temp = int(temp) / 1.00   # Original example said to use integer, but it is not needed for this script. It causes output to only be whole number.
        temp = str(round(temp, 2))
        temp = str(temp)
        return temp

# Print output to terminal
    print("Temp: " + read_temp() + "F")

# Print output to LCD
    lcd.write_string("Temp: " + read_temp() + "F")
    sleep(3)

    lcd.clear()
    sleep(0.5)
    lcd.close(clear=True)