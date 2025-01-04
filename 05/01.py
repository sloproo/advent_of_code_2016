import hashlib

def lue(tiedosto: str) -> str:
    with open(tiedosto) as f:
        return f.readline().strip()
    
id = lue("input.txt")
i = 0
passu = ""
while len(passu) < 8:
    sana = id + str(i)
    hasa = hashlib.md5((id + str(i)).encode()).hexdigest()
    if hasa[:5] == "00000":
        passu += hasa[5]
        print(f"Löytyi {hasa[5]}")
    i += 1

print(passu)
