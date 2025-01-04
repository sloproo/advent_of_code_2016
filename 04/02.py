import string

def lue(tiedosto: str) -> list:
    huoneet = []
    with open(tiedosto) as f:
        for r in f:
            r = r.strip()
            kirjainrimpsu = r[:-11]
            tarkistus = r[-6:-1]
            kirjaimet = {k: r.count(k, 0, -7) for k in string.ascii_lowercase}
            kirjaimet = dict(sorted(kirjaimet.items(), key= lambda x: x[1], reverse= True))
            numero = int(r[-10:-7])
            huoneet.append((kirjaimet, tarkistus, numero, kirjainrimpsu))
    return huoneet

def tarkista(huoneet: list) -> list:
    oikeat = []
    for huone in huoneet:
        kirjaimet, tarkistus, numero, kirjainrimpsu = huone
        for i in range(5):
            if kirjaimet[tarkistus[i]] != list(kirjaimet.values())[i]:
                break
        else:
            oikeat.append((kirjainrimpsu, numero))
    return oikeat
                
def dekoodaa(oikeat: list) -> list:
    nimet = []
    for oikea in oikeat:
        sana = ""
        kirjaimet, luku = oikea
        for kirjain in kirjaimet:
            if kirjain == "-":
                sana += " "
            else:
                sana += string.ascii_lowercase[
                    (string.ascii_lowercase.find(kirjain) + luku) \
                        % len(string.ascii_lowercase)]
        nimet.append((sana, luku))
    return nimet

huoneet = lue("input.txt")
oikeat = tarkista(huoneet)
dekoodatut = dekoodaa(oikeat)
lajitellut = sorted(dekoodatut)
for l in lajitellut:
    if "north" in l[0]:
        print(l)
