"""Kirjoita Auto-luokka, jonka ominaisuuksina
ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja
kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin
arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava
automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton
(rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen
jälkeen luodun auton kaikki ominaisuudet."""

class Auto:
	def __init__(self, license_plate, max_speed):
		self.license_plate = license_plate
		self.max_speed = max_speed
		self.current_speed = 0
		self.distance_traveled = 0

if __name__ == "__main__":

	mun_Auto = Auto( "ABC-123", 142)

	print(f"Rekisterinmero: {mun_Auto.license_plate}")
	print(f"huippuvaihde: {mun_Auto.max_speed} km/h")
	print(f"Nykyinen nopeus: {mun_Auto.current_speed} km/h")
	print(f"Kuljettu matka: {mun_Auto.distance_traveled} km")





