def lue(tiedosto: str) -> list:
    viivat = []

    with open(tiedosto) as f:
        while True:
            kolmikko = []
            for _ in range(3):
                rivi = f.readline()
                if rivi == "":
                    return viivat
                kolmikko.append([int(n) for n in rivi.strip().split()])
            for i in range(3):
                viivat.append([kolmikko[j][i] for j in range(3)])


viivatriot = lue("input.txt")

kelvolliset = []
for trio in viivatriot:
    if trio[0] < trio[1] + trio[2] and trio[1] < trio[0] + trio[2] and \
    trio[2] < trio[0] + trio[1]:
        kelvolliset.append(trio)
    else:
        continue

print(len(kelvolliset))
