from abc import ABC, abstractmethod

# Az Autó absztrakt osztály melynek két leszármazottja van

class Auto(ABC):
    # Konstruktor
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.berelve = False  # Alapértelmezetten nincs bérbe adva

    # Visszatér az autó szöveges reprezentációjával.
    def __str__(self):
        return f"{self.tipus} ({self.rendszam}) - {self.berleti_dij} Ft/nap"

    # Visszaadja az autó rendszámát.
    def GetRendszam(self):
        return self.rendszam

    # Visszaadja az autó márkáját, és típusát.
    def GetTipus(self):
        return self.tipus

    # Visszaadja az autó napi bérleti díját.
    def GetBerletiDij(self):
        return self.berleti_dij
    
    # Megmondja, hogy az autó jelenleg bérbe van-e adva.
    def IsBerelve(self):
        return self.berelve

    # Beállítja, hogy az autó bérbe van-e adva.
    # allapot: True, ha bérbe adva; False, ha szabad
    def SetBerelve(self, allapot: bool):
        self.berelve = allapot

    # Absztrakt metódus, amit a gyermekosztályoknak kell megvalósítaniuk.
    # Az autó minden adatát szövegként adja vissza.
    @abstractmethod
    def GetAutoAdatok(self):
        pass