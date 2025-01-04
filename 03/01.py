def lue(tiedosto: str) -> list:
    viivat = []
    with open(tiedosto) as f:
        for r in f:
            viivat.append([int(n) for n in r.strip().split()])
    return viivat

viivatriot = lue("input.txt")

kelvolliset = []
for trio in viivatriot:
    if trio[0] < trio[1] + trio[2] and trio[1] < trio[0] + trio[2] and \
    trio[2] < trio[0] + trio[1]:
        kelvolliset.append(trio)
    else:
        continue

print(len(kelvolliset))
