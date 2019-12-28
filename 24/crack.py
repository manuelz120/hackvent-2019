#!/usr/bin/python3

key = []
xored_flag = []

with open('./rom.bin', 'rb') as keyfile:
    key = keyfile.read(23)

with open('./brcmfmac43430-sdio.bin', 'rb') as ramfile:
    ramfile.seek(0x58e94)
    xored_flag = ramfile.read(23)


flag = ""
for (k, e) in zip(key, xored_flag):
    flag += chr(k ^ e)

print(flag)