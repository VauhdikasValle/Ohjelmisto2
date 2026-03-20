class Luokkahuone:
    def __init__(self, koodi, istumapaikat, tykki, ilmastointi, taulut, co2):
        self.koodi = koodi
        self.istumapaikat = istumapaikat
        self.tykki = tykki
        self.ilmastointi = ilmastointi
        self.taulut = taulut
        self.co2 = co2
        self.valot = False

    def oppitunti(self):
        if not self.ilmastointi:
            print("Ilmanlaatu huononee.")
            self.co2 = self.co2*2

    def vaihdavalot(self, paalla):
        self.valot = paalla

    #def __str__(self): TAI
    def __repr__(self):
        return f"Luokkahuone on {self.koodi}:\n" \
           f" * paikkoja: {self.istumapaikat}\n" \
           f" * tykki: {self.tykki}\n" \
           f" * ilmastointi: {self.ilmastointi}\n" \
           f" * taulut: {self.taulut}\n" \
           f" * co2: {self.co2}\n" \
           f" * valot: {self.valot}\n"

kme562 = Luokkahuone("KME562", 40, "Epson jotain", None, 10, 700)
kme572 = Luokkahuone("KME572", 5, None, None, 1, 700)

print(kme562)
#print(kme572)
kme562.oppitunti()
kme562.vaihdavalot(True)
print(kme562)