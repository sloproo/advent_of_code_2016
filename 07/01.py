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

def etsi_abba(rimpsu: str) -> bool:
    for i in range(len(rimpsu) - 3):
        if rimpsu[i] == rimpsu[i+3] and rimpsu[i+1] == rimpsu[i+2] and \
        rimpsu[i] != rimpsu[i+1]:
            return True
    else:
        return False

rivit = lue("input.txt")
tls_osumia = 0

for muut, sulkujen_sisallot in rivit:
    for muu in muut:
        if etsi_abba(muu):
            muissa_abba = True
            break
    else:
        muissa_abba = False
    for sulku in sulkujen_sisallot:
        if etsi_abba(sulku):
            suluissa_abba = True
            break
    else:
        suluissa_abba = False
    if muissa_abba and not suluissa_abba:
        tls_osumia += 1

print(f"TLS-kelvollisia osoitteita on: {tls_osumia}")
