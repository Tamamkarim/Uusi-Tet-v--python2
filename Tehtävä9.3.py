"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa
parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran
kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
'Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus
on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan
2090 km."""

class Auto:
    def __init__(self, huippunopeus):
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0.0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

#
auto = Auto(150) # Luodaan auto, jonka huippunopeus on 150 km/h

# Nostetaan nopeutta vaiheittain
auto.kiihdyta(30)   # Nopeus: 0 + 30 = 30 km/h
auto.kiihdyta(70)   # Nopeus: 30 + 70 = 100 km/h
auto.kiihdyta(50)   # Nopeus: 100 + 50 = 150 km/h (huippunopeus)
print(f"Auton nopeus: {auto.nopeus} km/h") # Tulostaa: 150 km/h

# Hätäjarrutus
auto.kiihdyta(-200)   # Nopeus: 150 - 200 = 0 km/h (ei voi mennä alle 0)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")   # Tulostaa: 0 km/h


auto.kuljettu_matka = 2000     # Asetetaan lähtömatka 2000 km
auto.nopeus = 60     # Nopeus asetetaan 60 km/h
auto.kulje(1.5)     # Ajetaan 1,5 tuntia nykyisellä nopeudella (60 km/h)
print(f"Auton kuljettu matka: {auto.kuljettu_matka} km")    # Tulostaa:











