"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos
on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion
nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta
suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja
lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus
määräämällä nopeuden muutos -200 km/h ja tulosta
uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää."""


class Auto:
    def __init__(self, huippunopeus):
        self.huippunopeus = huippunopeus
        self.nopeus = 0
#päo
    def kiihdyta(self, muutos): #
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


auto = Auto(150)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus: {auto.nopeus} km/h")


auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
