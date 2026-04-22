import pandas as pd
import matplotlib.pyplot as plt

# 1. Naložimo podatke iz CSV datoteke (ločeno s podpičjem)
podatki = pd.read_csv(r'C:\Users\zikov\Downloads\creditcard-fraud.csv', sep=';')

# 2. Priprava podatkov za analizo
# Ustvarimo nov številski stolpec (1 = prevara, 0 = pošteno) za izračun povprečja
podatki['is_fraud_numeric'] = (podatki['is_fradulent'] == 'fraudulent').astype(int)

# 3. Analiza različnih dejavnikov tveganja in risanje tortnih grafikonov (pie charts)
faktorji = ['is_declined', 'foreign_transaction', 'high_risk_countries']

for faktor in faktorji:
    print(f"\nAnaliza faktorja: {faktor}")
    
    # Izračunamo in izpišemo odstotek prevar (povprečje) v terminal
    print(podatki.groupby(faktor)['is_fraud_numeric'].mean())
    
    # --- Priprava podatkov za tortni grafikon ---
    # Za torto preštejemo skupno število prevar za vsako kategorijo ('yes' in 'no')
    vsota_prevar = podatki.groupby(faktor)['is_fraud_numeric'].sum()
    
    # Narišemo tortni grafikon (pie chart)
    plt.figure(figsize=(6, 6))
    vsota_prevar.plot(
        kind='pie', 
        autopct='%1.1f%%', # Prikaže procente na torti (npr. 45.2%)
        startangle=90,     # Zavrti torto za lepši prikaz
        colors=['#ff9999','#66b3ff'], # Barve za 'no' in 'yes'
        textprops={'fontsize': 12}
    )
    
    plt.title(f"Porazdelitev prevar glede na: {faktor}", fontsize=14, fontweight='bold')
    plt.ylabel("") # Skrijemo oznako y-osi, ker pri torti ni potrebna
    
    # Prikažemo grafikon
    plt.show()