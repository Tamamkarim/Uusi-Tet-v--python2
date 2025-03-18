"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan
automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu
kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton
huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus
luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun
 aikana tehdään tunnin välein
seuraavat toimenpiteet:"""


import random

class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.huippu, self.nopeus + muutos))

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

# Luo
autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

# Kilpailu
while max(auto.matka for auto in autot) < 1000:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)


for auto in autot:
    print(f"{auto.rek} | Huippu: {auto.huippu} km/h | Matka: {auto.matka:.1f} km")

