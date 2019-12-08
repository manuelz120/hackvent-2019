#!/usr/bin/python3
import sys

encrypted_flag = r"SlQRUPXWVo\Vuv_n_\ajjce"
encrypted_ccards = [r"QVXSZUVY\ZYYZ[a", r"QOUW[VT^VY]bZ", r"SPPVSSYVV\YY_\\]", r"RPQRSTUVWXYZ[\]^", r"QTVWRSVUXW[_Z`\b]"]

def decrypt(input, initialShift):   
    shift = initialShift
    output = ""

    for c in input:
        target = ord(c) - shift
        try:
            output += chr(target)
        except:
            break

        shift += 1
    
    return output

for encrypted_card in encrypted_ccards:
    decrypted = decrypt(encrypted_card, 30)
    if len(decrypted) == len(encrypted_card):
        print(decrypted)

print("Flag: HV19{%s}" % (decrypt(encrypted_flag, 30)))
