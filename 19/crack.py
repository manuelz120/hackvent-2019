#!/usr/bin/python
# coding=utf-8
from pwn import *
import json

with open ('emojis.json') as json_file:
    emojis = json.load(json_file)

    for emoji in emojis:
        p = process('./ch19')
        print(p.recvuntil('🔒 ➡️ 🎅🏻⁉️ ➡️ 🎄🚩 '))
        p.sendline(emoji.encode('utf-8'))
        output = p.readall()
        
        if not "👎" in output:
            print("Done: " + emoji)
            print(output)
            break
    