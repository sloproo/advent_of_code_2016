import re

class Ruutu:
    def __init__(self):
        self.naytto = []
        self.korkeus = 6
        self.leveys = 50
        for _ in range(self.korkeus):
            self.naytto.append([" " for _ in range(self.leveys)])
    
    def piirra_kulmio(self, x: int, y: int):
        for pysty in range(y):
            for vaaka in range(x):
                self.naytto[pysty][vaaka] = "#"
    
    def rivisiirto(self, rivi_nro: int, siirto: int):
        uusi_rivi = ["" for _ in range(self.leveys)]
        for x in range(self.leveys):
            uusi_rivi[(x + siirto) % self.leveys] = self.naytto[rivi_nro][x]
        self.naytto[rivi_nro] = uusi_rivi
    
    def pystysiirto(self, sarake_nro: int, siirto: int):
        pystysarake = [self.naytto[i][sarake_nro] for i in range(self.korkeus)]
        uusi_sarake = ["" for _ in range(self.korkeus)]
        for y in range(self.korkeus):
            uusi_sarake[(y + siirto) % self.korkeus] = pystysarake[y]
        for y in range(self.korkeus):
            self.naytto[y][sarake_nro] = uusi_sarake[y]

    def visualisoi(self):
        for y in range(self.korkeus):
            print("".join(self.naytto[y]))
    
    def laske_akt_pikselit(self):
        aktiivisia = 0
        for y in range(self.korkeus):
            aktiivisia += self.naytto[y].count("#")
        return aktiivisia

    def toteuta_ohjeet(self, tiedosto: str):
        with open(tiedosto) as f:
            for r in f:
                if "rect" in r:
                    kulmion_leveys = int(re.search(" [0-9]+x", r).group()[1:-1])
                    kulmion_korkeus = int(re.search("x[0-9]+", r).group()[1:])
                    self.piirra_kulmio(kulmion_leveys, kulmion_korkeus)
                elif "row" in r:
                    rivi = int(re.search("y=[0-9]+ ", r).group()[2:])
                    siirto = int(re.search("[0-9]+$", r).group())
                    self.rivisiirto(rivi, siirto)
                elif "column" in r:
                    sarake = int(re.search("x=[0-9]+ ", r).group()[2:])
                    siirto = int(re.search("[0-9]+$", r).group())
                    self.pystysiirto(sarake, siirto)

joo = Ruutu()
joo.toteuta_ohjeet("input.txt")
print(joo.laske_akt_pikselit())
