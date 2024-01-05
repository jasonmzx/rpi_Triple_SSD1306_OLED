import busio

# Hardware Module Drivers (By Adafruit)
import adafruit_ssd1306
import adafruit_tca9548a

class HardwareController:

    I2C_MULTIPLEXER = None
    I2C_Screens = []

    def __init__(self, i2c_bus):

        # Setup I2C MUX (TCA9548A Hardware Module) with I2C Bus from Raspberry PI
        self.I2C_MULTIPLEXER = adafruit_tca9548a.TCA9548A(i2c_bus)

    def add_screen(self, slot_number, width=128, height=64):

        if slot_number > 7:
            raise ValueError("TCA9548A Module only has 8 I2C slots! (0 - 7)")

        self.I2C_Screens[slot_number] = adafruit_ssd1306.SSD1306_I2C(width, height, self.I2C_MULTIPLEXER[slot_number])
    
    def __del__(self):
        print("TODO")