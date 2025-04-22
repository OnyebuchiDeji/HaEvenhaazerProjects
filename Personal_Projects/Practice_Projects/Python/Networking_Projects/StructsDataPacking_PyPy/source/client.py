"""
    Modified the original tutorial so that the determining of the format is done automatically using an fstring
    an len, for all strings.
    Also, the format is sent to the server, which then receives the format as a string and uses it
    to `unpack` the data_stream. It works well, and will certainly be useful!
"""


import socket as sck
import struct



def create_data_stream(fname:str, lname:str, age: int, gender:str, occupation: str, weight: float, identity: str):
    """Tuple assignment is not possible"""
    info = [fname, lname, age, gender, occupation, weight, identity]
    for index, item in enumerate(info):
        if type(item) == str:
            info[index] = item.encode()

    format_str = f"{len(fname)}s {len(lname)}s i s {len(occupation)}s f {len(identity)}s"
    print(format_str)
    data = struct.pack(format_str, *info)

    return data, format_str


def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    client.connect(("localhost", 9999))
    data_stream, format_str = create_data_stream("Eben", "Ayo-Metibemu", 19, "m", "Student", 87.52, "IEL")
    client.send(format_str.encode())
    client.send(data_stream)
    client.close()



if __name__ == "__main__":
    main()