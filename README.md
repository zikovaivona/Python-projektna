# Python-projektna

Program je namenjen analizi transakcij s kreditnimi karticami z namenom proučevanja in odkrivanja prevar (fraud).
Tukaj je natančen opis, kaj program počne, korak za korakom:
- Izračuna razmerje: Prešteje vse goljufive in vse poštene transakcije v datoteki ter izračuna njihovo medsebojno razmerje.
- Analizira dejavnike tveganja: Preveri, ali določeni dejavniki povečujejo možnost prevare. Natančneje izračuna, kolikšen odstotek transakcij je bil goljufiv, če:
      je bila transakcija predhodno zavrnjena (is_declined),
      je bila transakcija opravljena v tujini (foreign_transaction),
      je bila transakcija iz države z visokim tveganjem (high_risk_countries).
- Pripravi vizualizacijo (grafikon): Ustvari preprost stolpčni graf (bar chart), ki vizualno prikaže skupno število poštenih transakcij v primerjavi z goljufivimi.
- Interaktivno iskanje po trgovcu: Na koncu program postane interaktiven. V terminalu ti omogoča vnos ID-ja specifičnega trgovca (npr. 3160040998) in nato izpiše celotno njegovo zgodovino transakcij ter skupno število prevar, povezanih izključno s tem trgovcem. Program deluje, dokler ne vpišeš besede izhod.
# Avtorji
- Pia Tominec
- Ivona Zikova
