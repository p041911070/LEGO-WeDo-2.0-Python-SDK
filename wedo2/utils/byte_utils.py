
import struct



# Takes a value as an unsigned short, transforms it into an array of two bytes
# and adds those bytes to the end of the given bytearray 
def put_unsigned_short(array, value):
    short_array = struct.pack("<H", value)
    index = 0
    while array[index] != 0:
        index += 1

    array[index] = short_array[0]
    array[index+1] = short_array[1]


    
