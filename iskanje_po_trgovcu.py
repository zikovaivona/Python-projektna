import pandas as pd
import matplotlib.pyplot as plt

# 1. Naložimo podatke iz CSV datoteke (ločeno s podpičjem)
podatki = pd.read_csv(r'C:\Users\zikov\Downloads\creditcard-fraud.csv', sep=';')

# 2. Funkcija za iskanje transakcij določenega trgovca
def iskanje_po_trgovcu(merchant_id):
    # Podatke in vnos pretvorimo v tekst (string) za varno primerjavo
    trgovcu_podatki = podatki[podatki['merchan_id'].astype(str) == str(merchant_id)]
    
    # Preverimo, ali trgovec s tem ID-jem sploh obstaja
    if trgovcu_podatki.empty:
        print(f"Trgovec {merchant_id} ne obstaja ali nima transakcij.")
        return

    # Izpišemo celotno zgodovino za najdenega trgovca
    print(f"\nZgodovina transakcij za trgovca {merchant_id}:")
    print(trgovcu_podatki)
    
    # Preštejemo in izpišemo samo goljufive transakcije tega trgovca
    st_goljufivih = trgovcu_podatki[trgovcu_podatki['is_fradulent'] == 'fraudulent'].shape[0]
    print(f"\nŠtevilo goljufivih transakcij za trgovca {merchant_id}: {st_goljufivih}")

# 3. Neskončna zanka za interaktivni vnos uporabnika
while True:
    # Uporabnika prosimo za vnos ID-ja trgovca
    vnes_merchant_id = input("\nVpišite merchant_id (ali 'izhod' za izhod): ")
    
    # Če uporabnik vpiše 'izhod', prekinemo izvajanje programa
    if vnes_merchant_id.lower() == "izhod":
        print("Konec programa.")
        break
        
    # Kličemo funkcijo za iskanje z vnesenim ID-jem
    iskanje_po_trgovcu(vnes_merchant_id)