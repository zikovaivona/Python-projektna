import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Naloži podatke
df = pd.read_csv(r"C:\Users\Uporabnik\Downloads\creditcard-fraud (1).csv", sep=";")

# 2. Poenoti zapise
df.columns = df.columns.str.strip()

for col in ['is_fradulent', 'is_declined', 'foreign_transaction', 'high_risk_countries']:
    df[col] = df[col].astype(str).str.strip().str.lower()

# 3. Funkcija za izračun deleža goljufij
def fraud_rate(data, factor, value):
    subset = data[data[factor] == value]
    total = len(subset)
    if total == 0:
        return 0
    fraud = (subset['is_fradulent'] == 'fraudulent').sum()
    return fraud / total * 100

# 4. Dejavniki
factors = ['is_declined', 'foreign_transaction', 'high_risk_countries']
factor_labels = ['Predhodno zavrnjena', 'V tujini', 'Visoko tvegana država']

yes_rates = [fraud_rate(df, f, 'yes') for f in factors]
no_rates = [fraud_rate(df, f, 'no') for f in factors]

# 5. Stolpčni graf YES vs NO
x = np.arange(len(factor_labels))
width = 0.35

plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, yes_rates, width, label='yes')
bars2 = plt.bar(x + width/2, no_rates, width, label='no')

plt.xticks(x, factor_labels)
plt.ylabel('Delež goljufivih transakcij (%)')
plt.title('Delež goljufij glede na dejavnike tveganja')
plt.legend()

# 6. Vrednosti nad stolpci
for bar in list(bars1) + list(bars2):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 1,
        f'{height:.1f}%',
        ha='center'
    )

plt.ylim(0, 110)
plt.tight_layout()
plt.show()