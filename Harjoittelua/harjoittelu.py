class Koira:
    def __init__(self, uusiNimi, uusiSyntymävuosi):
        self.nimi = uusiNimi
        self.syntymävuosi = uusiSyntymävuosi



koira = Koira(uusiNimi = "Musti", uusiSyntymävuosi = 2019)
# koira.nimi = "Musti"
# koira.syntymävuosi = 2019

print(f"Hau Hau on {koira.nimi} ja syntynyt {koira.syntymävuosi}")
