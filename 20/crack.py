#!/usr/bin/python

scrambled_flag =  map(chr,[0xCE, 0x55, 0x95, 0x4E, 0x38, 0xC5, 0x89, 0xA5, 0x1B, 0x6F, 0x5E, 0x25,
                0xD2, 0x1D, 0x2A, 0x2B, 0x5E, 0x7B, 0x39, 0x14, 0x8E, 0xD0, 0xF0, 0xF8,
                0xF8, 0xA5])

flag = scrambled_flag
file_offset = 0x1337

with open('./505Retail.PUP', 'rb') as f:
    while file_offset != 0x1714908:
        f.seek(file_offset)
        key = f.read(len(scrambled_flag))

        newflag = ""
        count = 0
        for char in flag:
            newflag += chr(ord(char) ^ ord(key[count]))
            count += 1

        flag = newflag
        file_offset += 0x1337

print(flag)