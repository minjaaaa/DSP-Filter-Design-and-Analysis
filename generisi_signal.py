import numpy as np
import csv
import random

# Parametri simulacije
pocetna_udaljenost = 200.0 # cm
krajnja_udaljenost = 10.0  # cm
broj_uzoraka = 500

# 1. Idealan signal (vozilo se ravnomerno približava prepreci)
idealni_signal = np.linspace(pocetna_udaljenost, krajnja_udaljenost, broj_uzoraka)

# 2. Dodavanje mernog šuma (variranje senzora)
sum_merenja = np.random.normal(0, 1.5, broj_uzoraka) # Gausov šum, devijacija 1.5 cm
zavrsni_signal = idealni_signal + sum_merenja

# 3. Dodavanje impulsnog šuma (ekstremni pikovi)
broj_pikova = 25 # Koliko lažnih očitavanja želimo
indeksi_pikova = random.sample(range(broj_uzoraka), broj_pikova)

for i in indeksi_pikova:
    # Simuliramo gubljenje eha (nerealno velika udaljenost) ili refleksiju od poda (nerealno mala)
    if random.choice([True, False]):
        zavrsni_signal[i] += random.uniform(80, 150) 
    else:
        zavrsni_signal[i] -= random.uniform(40, zavrsni_signal[i] - 2) 

# HC-SR04 senzor fizički meri otprilike od 2 do 400 cm
zavrsni_signal = np.clip(zavrsni_signal, 2.0, 400.0) 

# 4. Čuvanje u CSV fajl
with open('ultrazvucni_signal.csv', mode='w', newline='') as fajl:
    writer = csv.writer(fajl)
    writer.writerow(['Vreme_indeks', 'Udaljenost_cm'])
    for i in range(broj_uzoraka):
        writer.writerow([i, round(zavrsni_signal[i], 2)])

print("Fajl 'ultrazvucni_signal.csv' je uspešno kreiran!")