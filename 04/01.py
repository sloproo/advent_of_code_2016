import string

def lue(tiedosto: str) -> list:
    huoneet = []
    with open(tiedosto) as f:
        for r in f:
            r = r.strip()
            tarkistus = r[-6:-1]
            kirjaimet = {k: r.count(k, 0, -7) for k in string.ascii_lowercase}
            kirjaimet = dict(sorted(kirjaimet.items(), key= lambda x: x[1], reverse= True))
            numero = int(r[-10:-7])
            huoneet.append((kirjaimet, tarkistus, numero))
    return huoneet

def tarkista(huoneet: list) -> int:
    summa = 0
    for huone in huoneet:
        kirjaimet, tarkistus, numero = huone
        for i in range(5):
            if kirjaimet[tarkistus[i]] != list(kirjaimet.values())[i]:
                break
        else:
            summa += numero

    return summa
                
                

huoneet = lue("input.txt")
print(tarkista(huoneet))
pass

