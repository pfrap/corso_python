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
titleB_FName = 'titleBasics.tsv.bz2'
titleP_FName = 'titlePrincipals.tsv.bz2'
nameB_FName = 'nameBasic.tsv.bz2'

dfTitleBasics = pd.read_csv(
    titleB_FName,
    #  compression='gzip',
    sep='\t',
    low_memory=False,
    memory_map=True,
    na_values='\\N')
print(dfTitleBasics.head())
print(dfTitleBasics.shape)
print(dfTitleBasics.columns)

dfTitlePrincipals = pd.read_csv(
    titleP_FName,
    #  compression='gzip',
    sep='\t',
    low_memory=False,
    memory_map=True,
    na_values='\\N')
print(dfTitlePrincipals.head())
print(dfTitlePrincipals.shape)
print(dfTitlePrincipals.columns)

dfName = pd.read_csv(
    nameB_FName,
    #  compression='gzip',
    sep='\t',
    low_memory=False,
    memory_map=True,
    na_values='\\N')
print(dfName.head())
print(dfName.shape)
print(dfName.columns)

# 2. Eliminare la colonna `job` dal dataframe `dfTitlePrincipals` e modificare
# il dataframe `dfName` perché contenga le sole colonne `nconst`, `primaryName`,
# `birthYear` e verificare l'avvenuta modifica.
dfTitlePrincipals.drop(columns=['job'], inplace=True)
print(dfTitlePrincipals.columns)
dfName = dfName[['nconst', 'primaryName', 'birthYear']]
print(dfName.columns)

# 3. Fondere i dataset `dfTitlePrincipals` e `dfName` nel nuovo dataframe `dfPN`,
# sfruttando il valore contenuto nelle colonne `nconst` e preservando il numero
# di osservazioni presenti nel dataframe `dfTitlePrincipals`. Successivamente
# si fondano il dataframe `dfTitleBasics` e `dfPN` nel nuovo dataframe `dfBPN`
# avendo cura che siano presenti tutti e soli i record presenti in entrambi i
# dataframe.
# Ad ogni passaggio si verifichi che la numerosità dei record sia concorde con
# quanto richiesto.
print('dfTitlePrincipals {} dfName {}'.format(dfTitlePrincipals.shape,
                                              dfName.shape))
dfPN = pd.merge(dfTitlePrincipals, dfName, on='nconst', how='left')
# left to preserve higher number of rows in dfTitlePrincipals
print(dfPN.shape)

dfBPN = pd.merge(dfTitleBasics, dfPN, on='tconst', how='inner')
print(dfBPN.shape)
print(dfBPN.columns)
#  dfBPN.to_csv('titleAndName.tsv.bz2', index=False, sep='\t')

# 4. Utilizzando il dataframe `dfBPN`, si individui il nome dell'attore che ha
# recitato in più film.
dfBPNgb = dfBPN.groupby(by=['primaryName']).count()
print(dfBPNgb.describe())
print("-"*50)
print(dfBPNgb)
id = dfBPNgb.idxmax()[0]
print(id)
print("-"*50)
print(dfBPN[dfBPN.nconst == id].primaryName.unique())

# 5. Si costruisca un nuovo dataframe che contenga tutti e soli i film che
# durino almeno 120 minuti e che siano di genere 'Comedy' o 'Drama'.
dfLongComedy = dfBPN[(dfBPN.runtimeMinutes >= 120) & (
    (dfBPN.genres == 'Comedy') | (dfBPN.genres == 'Drama'))]
print(dfLongComedy.shape)

# 6. Riprodurre il seguente grafico e salvarlo in un file di tipo `pdf`.
# Il grafico deve essere costruito a partire dalle informazioni contenute nel
# dataframe `dfBPN` e rappresenta il numero di film girati per ciascun genere.
# Chi non fosse riuscito a costruire il dataframe `dfBPN`, può usare il
# contenuto del file `titleAndName.tsv.bz2`, che riporta le medesime informazioni.
sBPNbyGenre = dfBPN.groupby(by='genres').tconst.count()
print("-"*50)
print(sBPNbyGenre)
sBPNbyGenre.sort_values(inplace=True)
print("-"*50)

print(sBPNbyGenre.head())

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.barh(sBPNbyGenre.index, sBPNbyGenre, color='r')
ax.set_title('Numerosità per genere')
ax.set_xlabel('numerosità')
plt.savefig('movieByGenre.pdf')
