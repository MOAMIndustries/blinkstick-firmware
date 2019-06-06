from intelhex import IntelHex   #pip install this

OUTPUT_FILE_NAME = "eeprom.hex"
SERIAL_FILE_NAME = "serial.txt"
MAJOR_VERSION = 1
MINOR_VERSION = 0
EEPROM_SIZE = 512
MODE = 2    #modes 0 & 1 are for RGB channels and not compatible with TA firmware, mode 2 is WS2812

OSCILATOR_CAL_ADDR = 0  #documented here for information, written to by firmware
SERIAL_ADDR =1
VERSION_ADDR = 22
MODE_ADDR = 21

##############################

serialNumber = 0
oHex = IntelHex()
for i in range(0, EEPROM_SIZE):
    oHex[i] = 0x00 # set EEPROM size

with open(SERIAL_FILE_NAME, 'r') as serialFile:
    serialTxt = serialFile.readline()
    serialNumber = int(serialTxt)
    serialNumber +=1
    serialFile.close()

with open(SERIAL_FILE_NAME, 'w') as serialFile:
    serialFile.write(str(serialNumber))
    serialFile.close()

serialString = "TV{0:012d}G".format(serialNumber)
versionString = "{0:02d}.{0:02d}".format(MAJOR_VERSION,MINOR_VERSION)
print("Serial: {} \nVersion: {}".format(serialString,versionString))

oHex.puts(SERIAL_ADDR, serialString)
oHex[MODE_ADDR] = MODE
oHex.puts(VERSION_ADDR, versionString)

oHex.write_hex_file(OUTPUT_FILE_NAME)



