import ClearTerminal
from Adatbetöltés.Adatbetolto import kolcsonzo_peldany


ClearTerminal.clear_terminal()


# A felhasználói menüt megvalósító programrész

def Menu():
    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ MENÜ ---")
        print("1 - Autó bérlése")
        print("2 - Bérlés lemondása")
        print("3 - Aktuális bérlések listázása")
        print("0 - Kilépés")

        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            rendszam = input("Add meg a bérelni kívánt autó rendszámát: ").upper()
            datum = input("Add meg a bérlés napját (pl. 2025-06-01): ")
            eredmeny = kolcsonzo_peldany.AutoBerles(rendszam, datum)
            print(eredmeny)

        elif valasztas == "2":
            rendszam = input("Add meg a lemondandó bérlés rendszámát: ").upper()
            datum = input("Add meg a bérlés dátumát: ")
            eredmeny = kolcsonzo_peldany.BerlesLemondas(rendszam, datum)
            print(eredmeny)

        elif valasztas == "3":
            print("\nAktív bérlések:")
            print(kolcsonzo_peldany.OsszesBerlesListazasa())

        elif valasztas == "0":
            print("Kilépés a programból...")
            break

        else:
            print("Érvénytelen opció, kérlek válassz újra!")

# A program belépési pontja
if __name__ == "__main__":
    Menu()

