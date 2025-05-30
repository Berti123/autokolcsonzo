from Osztályok.Berles import Berles

# Az autókölcsönzőt reprezentáló osztály, amely kezeli az autókat és a bérléseket (mint egy igazi autókölcsönző maga)


class Autokolcsonzo:
    def __init__(self, nev):
        # A kölcsönző neve, az autók és a bérlések listája
        self.nev = nev
        self.autok = []
        self.berlesek = []

    # Autó hozzáadása a kölcsönzőhöz
    def AutoHozzaadas(self, auto):
        self.autok.append(auto)

    # Autó bérlése megadott rendszámmal és dátummal
    def AutoBerles(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if self.Elerheto(rendszam, datum):
                    berles = Berles(auto, datum)
                    self.berlesek.append(berles)
                    return f"Sikeres bérlés. Ár: {auto.berleti_dij} Ft"
                else:
                    return "Ez az autó már bérlés alatt áll erre a napra."
        return "Nem található ilyen rendszámú autó."

    # Bérlés lemondása adott rendszámmal és dátummal
    def BerlesLemondas(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return "A bérlés sikeresen le lett mondva."
        return "Nincs ilyen bérlés."

    # Összes aktuális bérlés listázása
    def OsszesBerlesListazasa(self):
        if not self.berlesek:
            return "Nincsenek aktív bérlések."
        lista = []
        for berles in self.berlesek:
            lista.append(f"{berles.auto.rendszam} - {berles.auto.tipus} - {berles.datum}")
        return "\n".join(lista)

    # Ellenőrzi, hogy adott rendszámú autó szabad-e a megadott napon
    def Elerheto(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                return False
        return True