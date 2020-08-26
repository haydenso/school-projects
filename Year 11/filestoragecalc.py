def fileStorageCalc(h, w, bit):
    TOTAL_PIXELS = h * w
    FILESIZE = TOTAL_PIXELS * bit
    # FILESIZE is in bytes
    KB = FILESIZE/1024
    MB = KB/1000
    return KB, MB

while True:
    height = input("Input number of pixels high: ")
    width = input("input width in pixels: ")
    bitdepth = input("Input colordepth in bits: ")
    result = fileStorageCalc(height, width, bitdepth)       #result in tuple
    print("Filesize is " + str(result[0]) + "KB")
    print("Or " + str(result[1]) + "MB")
    break