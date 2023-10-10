import pandas as pd
import matplotlib.pyplot as plt

# 1. Caricare i dati contenuti nelle sole colonne 'country', 'year',
# 'population', 'gdp', 'primary_energy_consumption', 'energy_per_capita'
# del file `energiesPerCountry.csv` nel dataframe `dfEnergy` e stampare a video
# le prime righe del dataframe insieme alle sue dimensioni.
#dfEnergy=pd.read_csv(
#	"energiesPerCountry.csv",
#	use_cols=)

dfEnergy=pd.read_csv("energiesPerCountry.csv",
	usecols=["country","year","population" ,"gdp", "primary_energy_consumption","energy_per_capita"],
	low_memory=False)
print(dfEnergy.head())
print(dfEnergy.shape)


# 2. Si aggiunga al dataframe `dfEnergy` la colonna 'epc' che deve contenere il 
# rapporto tra l'energia consumata `primary_energy_consumption` moltiplicata
# per 10^9 ed il numero di abitanti `population`

dfEnergy["epc"]=dfEnergy["primary_energy_consumption"]*(10**9)*dfEnergy["population"]
print(dfEnergy)

"""
dfEnergy['epc'] = (dfEnergy.primary_energy_consumption *
                   1E9) / dfEnergy.population
print(dfEnergy.epc - dfEnergy.energy_per_capita)
"""

# 3. Caricare nel dataframe `dfTemp` i dati contenuti nel file
# `temperaturesPerCountry.csv`
dfTemp=pd.read_csv("temperaturesPerCountry.csv",
	sep=":",
	low_memory=False)
print(dfTemp.head())
print(dfTemp.shape)


# 4. Dopo aver immagazzinato nella variabile `tempYearMax` l'ultimo anno
# presente nel dataframe `dfTemp` (valore massimo della colonna `year`),
# costruire un nuovo datframe `dfEnergyCut` che contenga tutte e sole le
# osservazioni presenti nel dataframe `dfEnergy` e che abbiano come anno
# di osservazione un anno inferiore o uguale al valore della variabile
# `tempYearMax`
print("-"*50)
print("-"*50)

tempYearMax=dfTemp.iloc[dfTemp["year"].idxmax()]["year"]
print(tempYearMax)

dfEnergyCut=dfEnergy[dfEnergy["year"]<=tempYearMax]
print(dfEnergyCut.head())


# 5. Creare un nuovo dataframe `dfTempYC` che contenga il valor medio della
# temperatura per ciascuna nazione per ciascun anno.

dfTempYC=dfTemp.groupby(by=["Country", "year"], as_index=False).mean()
print("-"*50)
print(dfTempYC)



# 6. Aggiungere nei due dataframe `dfEnergyCut` e `dfTempYC` una nuova
# variabile chiamata `country_year` ottenuta dalla concatenazione del valore
# della variabile country e di quella `year` considerata come stringa.
# Ad esempio se la prima contiene 'Italia' e la seconda 2001 si deve ottenere
# 'Italia2001'.
# Successivamente, fondere i due dataframe `dfEnergyCut` e `dfTempYC` in un
# nuovo dataframe `dfFuso` sfruttando i valori  contenuti nelle variabili
# `country_year`. Se ne stampino a video le principali statistiche.

dfTempYC["country_year"]=dfTempYC["Country"]+(dfTempYC["year"].astype(str))
print(dfTempYC.head())
dfEnergyCut["country_year"]=dfEnergyCut["country"]+(dfEnergyCut["year"].astype(str))
print(dfEnergyCut.head())

dfFuso=pd.merge(dfTempYC,dfEnergyCut, on="country_year", how="inner")
print(dfFuso.describe())
print(dfFuso.head())
print(dfFuso.columns)


# 7. Riprodurre il seguente grafico e salvarlo in un file di tipo `pdf`.
# Il grafico deve essere costruito a partire dalle informazioni contenute nel
# dataframe `dfFuso` e rappresenta il legame tra la temperatura media e il
# consumo di energia pro capite `epc`. Chi non fosse riuscito a costruire il
# dataframe `dfFuso`, può usare il contenuto del file `dfFuso.csv`, che
# riporta le medesime informazioni.


fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
ax.scatter(dfFuso["AverageTemperature"],dfFuso["energy_per_capita"],
	linewidth=1,
	color="tomato", label="Scatter1")
ax.set_title("Grafico di prova")
ax.set_xlabel("Temperatura media")
ax.set_ylabel("Energy per capita")
ax.legend()
fig.savefig("provapietro.pdf")
plt.show()