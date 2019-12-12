#!/usr/bin/python3

encrypted_flag = "6klzic<=bPBtdvff'yFI~on//N"

decrypted_flag = "HV19{"

for i in range(len(encrypted_flag)):
    char = chr(ord(encrypted_flag[i]) ^ (6 + i))
    decrypted_flag += char

decrypted_flag += '}'
print(decrypted_flag)
