# 1. Caricare i dati contenuti nel file `movies.txt` nel dataframe
# `dfMovies` e creare la serie `sGenres` contenente un'unica copia
# per ogni genere associato ai film presenti nel file.

import pandas as pd
import matplotlib.pyplot as plt

dfMovies=pd.read_csv("movies.txt",
	sep="\t",
	skiprows=7,
	low_memory=False)
print(dfMovies.head())

sGenres1=dfMovies["genre1"].dropna()
sGenres2=dfMovies["genre2"].dropna()
sGenres3=dfMovies["genre3"].dropna()

listaGeneri=[]
for n in sGenres1:
	listaGeneri.append(n)
for n in sGenres2:
	listaGeneri.append(n)
for n in sGenres3:
	listaGeneri.append(n)	
	
listaGeneri=set(listaGeneri)
dizGeneri={}
i=0
for n in listaGeneri:
	dizGeneri[i]=n
	i+=1
sGenres=pd.Series(dizGeneri)
print(sGenres)


# 2. A partire dal dataframe  `dfMovie`, creare il dataframe
# `dfComedy` che contenga tutti i film per cui il genere 'Comedy'
# sia presente in almeno uno dei tre generi associati al record
# stesso, e se ne stampi a video il numero di righe e colonne.
dfComedy=dfMovies[(dfMovies["genre1"]=="Comedy")|(dfMovies["genre2"]=="Comedy")|(dfMovies["genre3"]=="Comedy")]
print(dfComedy.shape)

# 3. Caricare i dati contenuti nel file `ratings.txt` nel dataframe
# `dfRatings` e stampare a video il riassunto delle principali statistiche
# del contenuto del dataframe.
dfRatings=pd.read_csv("ratings.txt",
	sep="\t",
	low_memory=False,
	)
print(dfRatings.head())
print(dfRatings.describe())

# 4. Aggiungere al dataframe `dfRatings` una nuova colonna contenente
# l'indice 'rPesato', ottenuto dal prodotto dei valori contenuti nelle
# colonne `averageRating` e `numVotes`.
dfRatings["rPesato"]=dfRatings["averageRating"]*dfRatings["numVotes"]
print(dfRatings)
# 5. Costruire due nuovi dataframe `dfRatedMovies` e `dfOnlyRatedMovies`
# per fusione dei dataframe `dfMovies` e `dfRatings`.
# Nel dataframe `dfRatedMovies` dovranno essere presenti tutti i 
# film presenti in `dfMovies`, mentre nel secondo dataframe
# `dfOnlyRatedMovies` dovranno essere presenti tutti e soli i film che hanno
# ricevuto la valutazione. Inoltre si stampino a video le dimensioni
# dei dataframe ottenuti.
dfRatedMovies=pd.merge(dfMovies,dfRatings, on="tconst", how="left")
print(dfRatedMovies)
dfOnlyRatedMovies=pd.merge(dfMovies,dfRatings, on="tconst", how="right")
print(dfOnlyRatedMovies)

# 6. A partire dal dataframe `dfOnlyRatedMovies`, costruire il dataframe 
# `dfGenreW` che dovrà contenere le somme dell'indice `rPesato` associato
# ai film raggruppate per anno e genere. Nell'uso della funzione groupby,
# si suggerisce l'utilizzo dell parametro aggiuntivo `as_index=False`
# che restituisce un dataframe con indice semplice anziché un multi-index.
# Inoltre, a partire dal nuovo dataframe, si costruisca il dataframe
# `trendAnimation` che contenga i soli film, il cui genere principale (`genre1`)
# è 'Animation'
dfGenreW=dfOnlyRatedMovies.groupby(by=["startYear", "genre1"], as_index=False).sum()
print(dfGenreW)
trendAnimation=dfGenreW[dfGenreW["genre1"]=="Animation"]
#print(trendAnimation)
# 7. Riprodurre il seguente grafico e salvarlo in un file di tipo `pdf`.
# Il grafico deve essere costruito a partire dalle informazioni contenute
# nell dataframe `dfGenreW` e sfruttando la serie dei generi `sGenres`.
# Chi non fosse riuscito a costruire il dataframe `dfGenreW` può usare il
# contenuto del file `summary.csv`, che riporta le medesime
# informazioni.
print("-"*50)

fig=plt.figure()
ax=fig.add_subplot(111)
for n in set(sGenres1):
	temp=dfGenreW[dfGenreW["genre1"]==n]
	ax.plot(temp["startYear"], temp["rPesato"],'o-', label=n)
	ax.legend()
fig.savefig("filepit.pdf")
plt.show()