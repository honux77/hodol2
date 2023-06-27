# read file from command line
# python snes-rom-info.py <rom-file>
# get filename from command line

# if no filename is given, exit
import sys

if len(sys.argv) < 2:
    print("Usage: python snes-rom-info.py <rom-file>")
    sys.exit(1)

filename = sys.argv[1]

'''
address | length | description
$FFC0   | 21     | Game title
$FFD5   | 1      | Rom speed
$FFD6   | 1      | Chipset
$FFD7   | 1      | Rom size 1 << N KB
$FFD8  | 1      | Ram size 1 << N KB
'''

# open file using with statement
with open(filename, "rb") as f:
    f.seek(0xFFC0)
    title = f.read(21)
    print(title.decode("utf-8"))
    f.seek(0xFFD5)
    speed = f.read(1)
    #print speed bit
    print(bin(int.from_bytes(speed, byteorder="big")))

    f.seek(0xFFD6)
    chipset = f.read(1)
    if chipset == b"\x00":
        print("ROM only")
    elif chipset == b"\x01":
        print("ROM + RAM")
    elif chipset == b"\x02":
        print("ROM + RAM + BAT")
    
    f.seek(0xFFD7)
    rom_size = f.read(1)
    print("ROM size: {} KB".format(1 << rom_size[0]))
    f.seek(0xFFD8)
    ram_size = f.read(1)
    print("RAM size: {} KB".format(1 << ram_size[0]))
