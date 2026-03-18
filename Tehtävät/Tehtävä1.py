class Luokkahuone():
    def __init__(self, tunnus, istumapaikat, tykki, ilmastointi, taulu, ikkuna):
        self.tunnus = tunnus
        self.istumapaikat = istumapaikat
        self.tykki = tykki
        self.ilmastointi = ilmastointi
        self.taulu = taulu
        self.ikkuna = ikkuna

    def __repr__(self):
        return  f"Luokkahuone on {self.tunnus}:\n" \
                f" * paikkoja: {self.istumapaikat}\n" \
                f" * tykki: {self.tykki}\n" \
                f" * ilmastointi: {self.ilmastointi}\n" \
                f" * taulu: {self.taulu}\n" \
                f" * ikkuna: {self.ikkuna}\n" \

kme562 = Luokkahuone("kme562",30,"Epson",None,10, 6)
kme572 = Luokkahuone("kme572", 29, None, None, 1, 6)

print(kme562)
print(kme572)

