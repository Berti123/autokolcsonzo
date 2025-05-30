from Osztályok.Auto import Auto

# Teherautó osztály, amely az Auto ősosztály leszármazottja

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, szallithato_tomeg: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.szallithato_tomeg = szallithato_tomeg
        
    # A teherautó információinak visszaadása szövegként
    def GetAutoAdatok(self) -> str:
        return (
            f"Teherautó - Rendszám: {self.rendszam}, "
            f"Típus: {self.tipus}, "
            f"Bérleti díj: {self.berleti_dij} Ft/nap, "
            f"A teherautóval szállítható rakomány tömegének maximuma: {self.szallithato_tomeg}, "
            f"Bérlés állapota: {'Igen' if self.berelve else 'Nem'}"
        )