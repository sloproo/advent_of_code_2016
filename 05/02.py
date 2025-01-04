import hashlib
import random
import string

def lue(tiedosto: str) -> str:
    with open(tiedosto) as f:
        return f.readline().strip()
    
id = lue("input.txt")
i = 0
passu = "________"

while "_" in passu:
    sana = id + str(i)
    hasa = hashlib.md5((id + str(i)).encode()).hexdigest()
    if hasa[:5] == "00000" and hasa[5] in "01234567":
        if passu[int(hasa[5])] == "_":
            passu = passu[:int(hasa[5])] + hasa[6] + passu[int(hasa[5])+1:]
            print(passu)
    i += 1

print(passu)
