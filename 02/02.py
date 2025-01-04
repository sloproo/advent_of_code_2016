def lue(tiedosto: str) -> list:
    ohjeet = []
    with open(tiedosto) as f:
        for r in f:
            ohjeet.append([m for m in r.strip()])
    return ohjeet

def liiku(liike: str, paikka: tuple[int, int]) -> tuple[int, int]:
    if liike == "U" and paikka[1] > 0 and nappis[paikka[1] -1][paikka[0]] != "X":
        return (paikka[0], paikka[1] -1)
    elif liike == "R" and paikka[0] < 4 and nappis[paikka[1]][paikka[0] +1] != "X":
        return (paikka[0] + 1, paikka[1])
    elif liike == "D" and paikka[1] < 4 and nappis[paikka[1] +1][paikka[0]] != "X":
        return (paikka[0], paikka [1] + 1)
    elif liike == "L" and paikka[0] > 0 and nappis[paikka[1]][paikka[0] -1] != "X":
        return (paikka[0] - 1, paikka[1])
    else:
        return paikka

nappis = [["X", "X", "1", "X", "X"], ["X", "2", "3", "4", "X"], ["5", "6", "7", "8", "9"],
          ["X", "A", "B", "C", "X"], ["X", "X", "D", "X", "X"]]
paikka = (0, 2)
koodi = ""

liikesarjat = lue("input.txt")
for liikesarja in liikesarjat:
    for liike in liikesarja:
        paikka = liiku(liike, paikka)
        print(f"Liikuttiin {liike}, ollaan paikassa {nappis[paikka[1]][paikka[0]]}")
        pass
    koodi += nappis[paikka[1]][paikka[0]]
    print(nappis[paikka[1]][paikka[0]])

print(koodi)
