from Osztályok.Autokolcsonzo import Autokolcsonzo
from Osztályok.Szemelyauto import Szemelyauto
from Osztályok.Teherauto import Teherauto
from Osztályok.Berles import Berles

# Az autókölcsönző adatokkal való feltöltését végző osztály ami mindent egybefűz, így a Main függvényben csak a menüt kell majd declarálni


# Autókölcsönző létrehozása
kolcsonzo = Autokolcsonzo("Gábor Dénes Egyetemi Kölcsönző")

# 3 autó példányosítása és hozzáadása
auto1 = Szemelyauto("GDE-123", "Hyundai i30", 10000, 5)
auto2 = Szemelyauto("GDF-321", "Renault ZOE", 9000, 4)
auto3 = Teherauto("BME-456", "Ford Transit", 20000, 2000)

kolcsonzo.AutoHozzaadas(auto1)
kolcsonzo.AutoHozzaadas(auto2)
kolcsonzo.AutoHozzaadas(auto3)

# 4 bérlés létrehozása és hozzáadása

berles1 = Berles(auto1, "2025-06-01")
berles2 = Berles(auto2, "2025-06-02")
berles3 = Berles(auto3, "2025-06-03")
berles4 = Berles(auto1, "2025-06-04")

kolcsonzo.berlesek.append(berles1)
kolcsonzo.berlesek.append(berles2)
kolcsonzo.berlesek.append(berles3)
kolcsonzo.berlesek.append(berles4)

# A kolcsonzo példány elérhetővé tétele importáláshoz
kolcsonzo_peldany = kolcsonzo