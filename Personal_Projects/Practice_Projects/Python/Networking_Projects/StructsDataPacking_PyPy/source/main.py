"""
    Demonstrates the use of the core module, `struct` to package binary data
    in a structured way.
    It can hence be used to package the data and sent it as a byte stream through a network.
    The advantage is that it gives the binary data a format. Hence one can know the position of specific
    pieces of data in the byte stream.

    The struct creation involves specifying a format and then package them in this format into the
    byte stream
"""

import struct


def eg1():
    """
      The number of i charachers represents the number of integers that will
      be in that stream
      you cannot add a value whose size range exceeds the specified data type.

      This same format specified will be used to extract the values.

      How the values are interpreted can be manipulated by the format one provides
    """
    print("\nExample 1\n")
    integers_byte_stream = struct.pack("iii", 10, 20, 30)
    shorts_byte_stream = struct.pack("hhh", 10, 20, 30)
    print("Integers Byte Stream: ", integers_byte_stream)
    print("Shorts Byte Stream: ", shorts_byte_stream)
    print("\nSizes are in bytes!")
    print("Size of an Integer: ", struct.calcsize("i"))
    print("Size of a Short: ", struct.calcsize("h"))

    #   Unpacking them
    a, b, c = struct.unpack("HHH", shorts_byte_stream)
    print("A: {}, B: {}, C: {}".format(a, b, c))

    shorts_stream = struct.pack("hh", 50, 700)
    #   Even unpacking the above shorts stream as a single integer
    #   Note it onlt works because the stream contains two values of type short
    #   and a short is 2 bytes, hence 2 shorts = 1 integer (4 bytes)
    v = struct.unpack("i", shorts_stream)
    print(v)

    print("\n'")

def eg2():
    company = b"OfEvenHaazer"
    day, month, year = 1, 1, 2022
    leng = True

    """
        The below are place holders
        The '12s' represents the length of the string, 'company'
        The '3i' represents 3 integers
        The '?' represents a boolean

    """
    byte_stream = struct.pack("12s 3i ?", company, day, month, year, leng)
    print(byte_stream)

    #   Decoding the byte stream
    strVal, dd, mm, yy, ver = struct.unpack("12s 3i ?", byte_stream)
    print("strVal: {}, dd: {}, mm: {}, yy: {}, ver: {}".format(strVal, dd, mm, yy, ver))
    print(struct.unpack("12s 3i ?", byte_stream))

    #   Can store the byte stream

    with open("data", "wb") as f:
        f.write(byte_stream)
    
    with open("data", "rb") as f:
        data = f.read()
    
    print("Just Read Stream Data From File:")
    print(struct.unpack("12s 3i ?", data))


def main():
    eg1()


if __name__ == "__main__":
    main()