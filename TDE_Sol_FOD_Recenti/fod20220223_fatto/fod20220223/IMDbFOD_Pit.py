import pandas as pd
import matplotlib.pyplot as plt


# 1. Caricare i dati contenuti nei tre file `titleBasics.tsv.bz2`,
# `titlePrincipals.tsv.bz2`, `nameBasic.tsv.bz2`, rispettivamente nei 3
# dataframe `dfTitleBasics`, `dfTitlePrincipals`, `dfName`.
# Si ricorda che pandas è in grado di caricare anche i file compressi con lo
# stesso metodo usato per leggere i file non compressi senza alcun parametro
# aggiuntivo. Inoltre, il parametro per poter associare il simbolo '\\N' al
# valore nan è `na_values`. Di ciascun dataframe si verifichi la forma,
# stampando a video i relativi valori ed il nome delle colonne.

dfTitleBasics=pd.read_csv(
	"titleBasics.tsv.bz2",
	sep="\t",
	na_values="\\N",
	low_memory=False,
	)
"""
print(dfTitleBasics.head())
print(dfTitleBasics.columns)
print(dfTitleBasics.shape)
"""
dfTitlePrincipals=pd.read_csv("titlePrincipals.tsv.bz2",
	sep="\t",
	na_values="\\N",
	low_memory=False
	)
"""	
print(dfTitlePrincipals.head())
print(dfTitlePrincipals.columns)
print(dfTitlePrincipals.shape)
"""
dfName=pd.read_csv("nameBasic.tsv.bz2",
	sep="\t",
	na_values="\\N",
	low_memory=False
	)
"""
print(dfName.head())
print(dfName.columns)
print(dfName.shape)
"""

# 2. Eliminare la colonna `job` dal dataframe `dfTitlePrincipals` e modificare
# il dataframe `dfName` perché contenga le sole colonne `nconst`, `primaryName`,
# `birthYear` e verificare l'avvenuta modifica.
print(dfTitlePrincipals.columns)
dfTitlePrincipals.drop(columns=["job"], inplace=True)
print(dfTitlePrincipals.columns)
print("-"*30)
print(dfName.columns)
dfName=dfName[["nconst","primaryName","birthYear"]]
print(dfName.head())
print("-"*30)

# 3. Fondere i dataset `dfTitlePrincipals` e `dfName` nel nuovo dataframe `dfPN`,
# sfruttando il valore contenuto nelle colonne `nconst` e preservando il numero
# di osservazioni presenti nel dataframe `dfTitlePrincipals`. Successivamente
# si fondano il dataframe `dfTitleBasics` e `dfPN` nel nuovo dataframe `dfBPN`
# avendo cura che siano presenti tutti e soli i record presenti in entrambi i
# dataframe.
# Ad ogni passaggio si verifichi che la numerosità dei record sia concorde con
# quanto richiesto.

print(f"dfTitlePrincipals {dfTitlePrincipals.shape}, dfName {dfName.shape}")
dfPN=pd.merge(dfTitlePrincipals, dfName, on="nconst", how="left" )
print(dfPN.head())
print(f"dfPN {dfPN.shape}")

print("-"*30)
dfBPN=pd.merge(dfTitleBasics, dfPN, on="tconst", how="inner")
print(f"dfBPN shape {dfBPN.shape}")
print(dfBPN.columns)

# 4. Utilizzando il dataframe `dfBPN`, si individui il nome dell'attore che ha
# recitato in più film.
dfBPNName=dfBPN.groupby(by=["primaryName"]).count()
winner=dfBPNName.idxmax()[0]
"""
print(dfBPNName)
print("-"*30)
print(f"{winner} è l'attore che ha recitato in piu' film.")
print("-"*30)
"""
# 5. Si costruisca un nuovo dataframe che contenga tutti e soli i film che
# durino almeno 120 minuti e che siano di genere 'Comedy' o 'Drama'.
newDF=dfBPN[(dfBPN["runtimeMinutes"]<120)& ((dfBPN["genres"]=="Drama")|(dfBPN["genres"]=="Comedy"))]
"""
print(newDF[["tconst", "genres", "runtimeMinutes"]])
"""
# 6. Riprodurre il seguente grafico e salvarlo in un file di tipo `pdf`.
# Il grafico deve essere costruito a partire dalle informazioni contenute nel
# dataframe `dfBPN` e rappresenta il numero di film girati per ciascun genere.
# Chi non fosse riuscito a costruire il dataframe `dfBPN`, può usare il
# contenuto del file `titleAndName.tsv.bz2`, che riporta le medesime informazioni.
print("-"*50)
print("-"*50)
print("-"*50)

dfGraf=dfBPN.groupby(by="genres").count()
dfGraf.sort_values(by="tconst", inplace=True)
print(dfBPN)
print("-"*30)
print(dfGraf)

fig= plt.figure(figsize=(10,10))
ax=fig.add_subplot()
ax.barh(dfGraf.index, dfGraf["tconst"], color="tomato", label="Grafichello")
ax.set_title("prova")
ax.legend()
plt.show()

"""
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.bar(dfGrafico.index, dfGrafico)
ax.set_title('Numerosità per genere')
ax.set_xlabel('numerosità')
plt.savefig('prova.pdf')
"""