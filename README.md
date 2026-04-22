# Python-projektna

Program je namenjen analizi transakcij s kreditnimi karticami z namenom proučevanja in odkrivanja prevar (fraud).
Tukaj je natančen opis, kaj program počne, korak za korakom:
- Analiza strukture prevar (Tortni grafikoni): Program najprej analizira tri ključne dejavnike tveganja (zavrnjene transakcije, tujina, visoko tvegane države) in za vsakega izriše tortni grafikon (pie chart). Ta prikazuje, kolikšen delež vseh prevar se je zgodil ob prisotnosti posameznega dejavnika.
- Primerjava deleža goljufij (Združen stolpčni graf): Izračuna in vizualizira natančen odstotek goljufivih transakcij. Ustvari napreden stolpčni graf, ki drug ob drugem primerja tveganje za prevaro, ko je dejavnik prisoten ('yes') in ko ga ni ('no').
- Pregled celotnega stanja (Stolpčni graf): Ustvari osnovni stolpčni graf (bar chart), ki vizualno prikaže absolutno skupno število vseh poštenih transakcij v primerjavi z goljufivimi v celotni bazi podatkov.
- Interaktivno iskanje po trgovcu: Na koncu program postane interaktiven. V terminalu ti omogoča vnos ID-ja specifičnega trgovca in nato izpiše celotno njegovo zgodovino transakcij ter prešteje, koliko prevar je bilo izvedenih pri tem trgovcu. Program deluje, dokler ne vpišeš besede izhod.
# Zmago
Za uporabo datotek je potrebno naložiti:
```bash
pip install pandas
pip install matplotlib
pip install numpy
```
# Avtorji
- Pia Tominec
- Ivona Zikova
