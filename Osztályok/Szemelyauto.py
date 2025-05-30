from Osztályok.Auto import Auto

# Személyautó osztály, amely az Auto ősosztály leszármazottja

class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, szemelyek_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.szemelyek_szama = szemelyek_szama
        
    # A személyautó információinak visszaadása szövegként
    def GetAutoAdatok(self) -> str:
        return (
            f"Személyautó - Rendszám: {self.rendszam}, "
            f"Típus: {self.tipus}, "
            f"Bérleti díj: {self.berleti_dij} Ft/nap, "
            f"Ülések száma: {self.szemelyek_szama}, "
            f"Bérlés állapota: {'Igen' if self.berelve else 'Nem'}"
        )