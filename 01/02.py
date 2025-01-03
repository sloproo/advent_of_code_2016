def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        askeleet_raaka = f.readline().strip().split(", ")
        askeleet = [(a[0], int(a[1:])) for a in askeleet_raaka]
    return askeleet

def liikkeet(paikka: tuple[int, int], suunta: str, askeleet: int, kaydyt: set) \
-> tuple[set, bool]:
    for _ in range(askeleet):
        if suunta == "N":
            paikka = (paikka[0], paikka[1] + 1)
        elif suunta == "E":
            paikka = (paikka[0] + 1, paikka[1])
        elif suunta == "S":
            paikka = (paikka[0], paikka[1] - 1)
        elif suunta == "W":
            paikka = (paikka[0] - 1, paikka[1])
        if paikka in kaydyt:
            print(f"Ollaan uudestaan paikassa {paikka}")
            print(f"Sen etäisyys lähtöpisteestä on {abs(paikka[0]) + abs(paikka[1])}")
            return (kaydyt, True, paikka)
        else:
            kaydyt.add(paikka)
    return (kaydyt, False, paikka)


askeleet = lue("input.txt")

paikka = (0, 0)
suunta = "N"
suunnat = "NESW"
kaydyt = {(0, 0)}

for a in askeleet:
    assert a[0] in ["L", "R"]
    if a[0] == "L":
        suunta = suunnat[(suunnat.find(suunta) - 1) % 4]
    else:
        suunta = suunnat[(suunnat.find(suunta) + 1) % 4]
    
    taaperrus = liikkeet(paikka, suunta, a[1], kaydyt)
    if taaperrus[1] == True:
        break
    else:
        kaydyt.update(taaperrus[0])
        paikka = taaperrus[2]

