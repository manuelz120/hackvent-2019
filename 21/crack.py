#!/usr/bin/python3

from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
import hashlib
import base64

potential_passwords = []

with open ('./rockyou.txt') as f:
    passwords = f.readlines()
    potential_passwords = list(filter(lambda x: len(x.strip()) == 16, passwords))


print("Found %d potential passwords" % len(potential_passwords))

santas_password = ""

for password in potential_passwords:
    x = 0xc58966d17da18c7f019c881e187c608fcb5010ef36fba4a199e7b382a088072f
    y = 0xd91b949eaf992c464d3e0d09c45b173b121d53097a9d47c25220c0b4beb943c
    d = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
    try:
        private_key = ECC.construct(curve='NIST P-256', d=int(d,16), point_x =x, point_y =y)
        santas_password = password.strip()
        break
    except:
        continue

print("Found santas password: %s" % santas_password)

encrypted_flag = "Hy97Xwv97vpwGn21finVvZj5pK/BvBjscf6vffm1po0="

def decrypt(encrypted, key, salt, rounds):
    encrypted_bytes = base64.decodebytes(encrypted.encode('utf-8'))
    key = hashlib.pbkdf2_hmac('sha256', key.encode('utf-8'), salt, rounds)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_bytes)
    return decrypted

flag = decrypt(encrypted_flag, santas_password, b'TwoHundredFiftySix', 256 * 256 * 256)
print(flag)