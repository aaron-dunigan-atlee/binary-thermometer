# Imports
from sense_hat import SenseHat

# Global variables
sense = SenseHat()

# Functions
def celsius_to_fahrenheit(celsius):
    """ Return fahrenheit as an integer. """
    fahrenheit = 1.8 * celsius + 32
    return int(fahrenheit)

def decimal_to_binary(num):
    """ Convert a decimal integer to a list of bits. """
    pow2 = 128
    binary_list = []
    while pow2 >= 1:
        if (num // pow2) == 1:
            binary_list.append(num // pow2)
            num = num - pow2
        else:
            binary_list.append(num // pow2)
        pow2 = pow2 // 2
    return binary_list

def display(bit_list):
    """
    Given a list of bits, turn the LED matrix
    white (0) and blue (1) to display the binary.
    """
    blue = (0,0,255)
    white = (255,255,255)
  
    row = 3
    column = 0
    while column < 8:
        if bit_list[column] == 0:
          sense.set_pixel(column, row, white)
        else:
          sense.set_pixel(column, row, blue)
        column = column + 1

# Main code
while True:
    temp_C = sense.get_temperature()
    temp_F = celsius_to_fahrenheit(temp_C)
    temp_bin = decimal_to_binary(temp_F)
    display(temp_bin)
