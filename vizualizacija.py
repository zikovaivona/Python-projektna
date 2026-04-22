import pandas as pd
import matplotlib.pyplot as plt

# 1. Naložimo podatke iz CSV datoteke (ločeno s podpičjem)
podatki = pd.read_csv(r"C:\Users\Uporabnik\Downloads\creditcard-fraud (1).csv", sep=";")

# 2. Vizualizacija podatkov
# Nastavimo velikost okna za grafikon
plt.figure(figsize=(10, 6))

# Preštejemo transakcije in narišemo stolpčni graf
podatki['is_fradulent'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])

# Nastavimo naslov in oznako navpične osi
plt.title("Število goljufivih in poštenih transakcij")
plt.ylabel("Število transakcij")

# Poravnamo besedilo pod stolpci vodoravno
plt.xticks(rotation=0)

# Prikažemo grafikon na zaslonu
plt.show()