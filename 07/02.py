import re

def lue(tiedosto: str) -> tuple[list, list]:
    with open(tiedosto) as f:
        palautettava = []
        for r in f:
            sulkujen_sisallot = [s[1:-1] for s in re.findall("\[[a-z]*\]", r.strip())]
            muut = [sana.replace("[", "").replace("]", "") for sana in
                    re.findall("^[a-z]*\[|\][a-z]*\[|\][a-z]+$", 
                               r.strip())]
            palautettava.append((muut, sulkujen_sisallot))
    return palautettava

def etsi_abat(rimpsu: str) -> list:
    abat = set()
    for i in range(len(rimpsu) - 2):
        if rimpsu[i] == rimpsu[i+2] and rimpsu[i] != rimpsu[i+1]:
            abat.add(rimpsu[i:i+3])
    return abat

def etsi_bab(rimpsu: str, abat: set) -> bool:
    for aba in abat:
        if aba[1] + aba[0] + aba[1] in rimpsu:
            return True
    else:
        return False

rivit = lue("input.txt")
ssl_osumia = 0

for muut, sulkujen_sisallot in rivit:
    abat = set()
    for muu in muut:
        abat.update(etsi_abat(muu))
    for sulku in sulkujen_sisallot:
        if etsi_bab(sulku, abat):
            ssl_osumia += 1
            break

print(f"SSL-kelvollisia osoitteita on: {ssl_osumia}")
