def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        askeleet_raaka = f.readline().strip().split(", ")
        askeleet = [(a[0], int(a[1:])) for a in askeleet_raaka]
    return askeleet

askeleet = lue("input.txt")

paikka = (0, 0)
suunta = "N"
suunnat = "NESW"

for a in askeleet:
    assert a[0] in ["L", "R"]
    if a[0] == "L":
        suunta = suunnat[(suunnat.find(suunta) - 1) % 4]
    else:
        suunta = suunnat[(suunnat.find(suunta) + 1) % 4]
    if suunta == "N":
        paikka = (paikka[0], paikka[1] + a[1])
    elif suunta == "E":
        paikka = (paikka[0] + a[1], paikka[1])
    elif suunta == "S":
        paikka = (paikka[0], paikka[1] - a[1])
    elif suunta == "W":
        paikka = (paikka[0] - a[1], paikka[1])
    else:
        raise AssertionError("Suunta outo")
    pass

print(f"Ollaan paikassa {paikka}")
print(f"Sen etäisyys lähtöpisteestä on {abs(paikka[0]) + abs(paikka[1])}")
