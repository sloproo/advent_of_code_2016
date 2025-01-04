def lue(tiedosto: str) -> list:
    sanat = []
    with open(tiedosto) as f:
        for r in f:
            sanat.append(r.strip())
    return sanat

sanat = lue("input.txt")
lukumaarat = {}
for i in range(len(sanat[0])):
    lukumaarat[i] = {}
    for sana in sanat:
        if sana[i] in lukumaarat[i]:
            lukumaarat[i][sana[i]] += 1
        else:
            lukumaarat[i][sana[i]] = 1

listana = []
for kohta in lukumaarat:
    lukumaarat[kohta] = dict(sorted(lukumaarat[kohta].items(), key= lambda x: x[1]))
    listana.append(sorted(lukumaarat[kohta].items(), key= lambda x: x[1]))

for kohta in listana:
    print(kohta[0][0], end="")
