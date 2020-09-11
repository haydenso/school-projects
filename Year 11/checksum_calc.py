def checksum(msg):
    decimal = sum([int(ord(bit)) for bit in msg]) % 256     # forumula for finding checksum in decimal
    hexd = hex(decimal)
    print(f"The checksum is {decimal} or {hexd}")

if __name__ == "__main__":
    message = str(input("Message: "))
    checksum(message)
