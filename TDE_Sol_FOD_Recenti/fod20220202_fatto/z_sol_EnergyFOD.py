import pandas as pd
import matplotlib.pyplot as plt

# 1. Caricare i dati contenuti nelle sole colonne 'country', 'year',
# 'population', 'gdp', 'primary_energy_consumption', 'energy_per_capita'
# del file `energiesPerCountry.csv` nel dataframe `dfEnergy` e stampare a video
# le prime righe del dataframe insieme alle sue dimensioni.

energyFile = 'energiesPerCountry.csv'
#  dfEnergy = pd.read_csv(energyFile)
dfEnergy = pd.read_csv(energyFile,
                       usecols=[
                           'country', 'year', 'population', 'gdp',
                           'primary_energy_consumption', 'energy_per_capita'
                       ])
print(dfEnergy.shape)
print(dfEnergy.head())

# 2. Si aggiunga al dataframe `dfEnergy` la colonna 'epc' che deve contenere il 
# rapporto tra l'energia consumata `primary_energy_consumption` moltiplicata
# per 10^9 ed il numero di abitanti `population`

dfEnergy['epc'] = (dfEnergy.primary_energy_consumption *
                   1E9) / dfEnergy.population
print(dfEnergy.epc - dfEnergy.energy_per_capita)

# 3. Caricare nel dataframe `dfTemp` i dati contenuti nel file
# `temperaturesPerCountry.csv`

tempFile = 'temperaturesPerCountry.csv'
dfTemp = pd.read_csv(tempFile, sep=':')
print(dfTemp)

# 4. Dopo aver immagazzinato nella variabile `tempYearMax` l'ultimo anno
# presente nel dataframe `dfTemp` (valore massimo della colonna `year`),
# costruire un nuovo datframe `dfEnergyCut` che contenga tutte e sole le
# osservazioni presenti nel dataframe `dfEnergy` e che abbiano come anno
# di osservazione un anno inferiore o uguale al valore della variabile
# `tempYearMax`

tempYearMax = dfTemp.year.max()
print(tempYearMax)

dfEnergyCut = dfEnergy[dfEnergy.year <= tempYearMax]
print(dfEnergyCut.year.describe())

# 5. Creare un nuovo dataframe `dfTempYC` che contenga il valor medio della
# temperatura per ciascuna nazione per ciascun anno.

dfTempYC = dfTemp.groupby(by=['Country', 'year'], as_index=False).mean()

# 6. Aggiungere nei due dataframe `dfEnergyCut` e `dfTempYC` una nuova
# variabile chiamata `country_year` ottenuta dalla concatenazione del valore
# della variabile country e di quella `year` considerata come stringa.
# Ad esempio se la prima contiene 'Italia' e la seconda 2001 si deve ottenere
# 'Italia2001'.
# Successivamente, fondere i due dataframe `dfEnergyCut` e `dfTempYC` in un
# nuovo dataframe `dfFuso` sfruttando i valori  contenuti nelle variabili
# `country_year`. Se ne stampino a video le principali statistiche.
dfTempYC['country_year'] = dfTempYC.Country + dfTempYC.year.astype(str)
print(dfTempYC.head())
print(dfTempYC.describe())

dfEnergyCut['country_year'] = dfEnergyCut.country + dfEnergyCut.year.astype(
    str)
print(dfEnergyCut.columns)

dfFuso = pd.merge(dfEnergyCut, dfTempYC, on='country_year', how='inner')
#  dfFuso.to_csv('dfFuso.csv', index=False)
print(dfFuso.describe())

# 7. Riprodurre il seguente grafico e salvarlo in un file di tipo `pdf`.
# Il grafico deve essere costruito a partire dalle informazioni contenute nel
# dataframe `dfFuso` e rappresenta il legame tra la temperatura media e il
# consumo di energia pro capite `epc`. Chi non fosse riuscito a costruire il
# dataframe `dfFuso`, può usare il contenuto del file `dfFuso.csv`, che
# riporta le medesime informazioni.

fig = plt.figure()
ax = fig.add_subplot(111)
#  ax.scatter(dfFuso.AverageTemperature, dfFuso.primary_energy_consumption)
ax.scatter(dfFuso.AverageTemperature, dfFuso.energy_per_capita)
ax.set_title('Consumo pro capite per stato')
ax.set_xlabel('Temperatura media [°C]')
ax.set_ylabel('Cosnumo energia [TWh]')
plt.savefig('temperaturaEnergia.pdf')
