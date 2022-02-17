import binascii
encoded = input('enter encoded message \n >)
encoded = binascii.unhexlify(encoded)
for xor_key in range(256):
    decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    if decoded.isprintable():
        print(xor_key, decoded)

