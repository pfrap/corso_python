### Esercizio 1

# La seguente struttura dati memorizza le informazioni sugli acquisti di caffe' in capsule effettuate da dei clienti.
# Ogni tupla contiene le informazioni su un'acquisto di un singolo tipo di capsula da parte di un cliente:
#   * il primo elemento della tupla corrisponde ad un valore numerico che identifica univocamente un cliente
#   * il secondo elemento della tupla corrisponde alla data in cui e' avvenuto l'acquisto
#   * il terzo elemento della tupla corrisponde ad una stringa che rappresenta il tipo di capsula acquistata (es., 'ristretto')
#   * il quarto elemento della tupla corrisponde ad un intero che rappresenta la quantita' di capsule acquistate dall'utente
#   * il quinto elemento della tupla corrisponde ad un float che rappresenta il costo di acquisto in euro di una singola capsula.

datiCapsule=[(5, '03/01/2019', 'lungo', 10, 1.41), (5, '03/01/2019', 'arabico', 40, 1.75), (5, '03/01/2019', 'normale', 20, 0.9), (5, '03/01/2019', 'ristretto', 50, 1.64), (15, '07/01/2019', 'lungo', 50, 1.35), (15, '07/01/2019', 'ristretto', 20, 1.63), (15, '07/01/2019', 'robusto', 40, 1.81), (14, '09/01/2019', 'decaffeinato', 40, 1.26), (17, '09/01/2019', 'decaffeinato', 30, 1.12), (17, '09/01/2019', 'normale', 40, 0.99), (17, '09/01/2019', 'lungo', 20, 1.59), (17, '09/01/2019', 'intenso', 20, 1.16), (2, '11/01/2019', 'decaffeinato', 30, 1.05), (2, '11/01/2019', 'robusto', 40, 1.96), (10, '13/01/2019', 'arabico', 30, 1.39), (10, '13/01/2019', 'decaffeinato', 30, 1.27), (10, '13/01/2019', 'lungo', 40, 1.77), (17, '14/01/2019', 'arabico', 30, 1.75), (17, '14/01/2019', 'robusto', 40, 1.65), (17, '14/01/2019', 'lungo', 10, 1.21), (17, '14/01/2019', 'intenso', 20, 1.28), (17, '14/01/2019', 'normale', 40, 0.93), (3, '16/01/2019', 'forte', 10, 1.41), (3, '16/01/2019', 'normale', 50, 1.0), (3, '16/01/2019', 'ristretto', 30, 1.79), (20, '21/01/2019', 'decaffeinato', 40, 1.02), (9, '22/01/2019', 'lungo', 10, 1.33), (18, '22/01/2019', 'normale', 10, 1.05), (18, '22/01/2019', 'forte', 40, 1.48), (18, '22/01/2019', 'ristretto', 30, 1.56), (18, '22/01/2019', 'robusto', 10, 1.98), (18, '22/01/2019', 'lungo', 50, 1.69), (13, '23/01/2019', 'lungo', 40, 1.75), (13, '23/01/2019', 'arabico', 20, 1.93), (13, '23/01/2019', 'decaffeinato', 10, 1.06), (13, '23/01/2019', 'forte', 10, 1.14), (7, '24/01/2019', 'lungo', 40, 1.35), (7, '24/01/2019', 'robusto', 10, 1.49), (7, '24/01/2019', 'normale', 40, 0.95), (7, '24/01/2019', 'decaffeinato', 50, 0.97), (7, '24/01/2019', 'arabico', 10, 2.02), (8, '24/01/2019', 'decaffeinato', 20, 1.22), (16, '24/01/2019', 'decaffeinato', 30, 1.17), (16, '24/01/2019', 'intenso', 50, 1.04), (16, '24/01/2019', 'robusto', 50, 1.87), (16, '24/01/2019', 'normale', 10, 0.82), (7, '27/01/2019', 'normale', 40, 0.91), (7, '27/01/2019', 'forte', 30, 1.06), (7, '27/01/2019', 'decaffeinato', 50, 1.21), (7, '27/01/2019', 'lungo', 30, 1.51), (7, '27/01/2019', 'intenso', 10, 1.04), (19, '27/01/2019', 'robusto', 20, 2.07), (19, '27/01/2019', 'arabico', 30, 1.63), (19, '27/01/2019', 'forte', 30, 1.09), (19, '27/01/2019', 'decaffeinato', 20, 0.95), (6, '28/01/2019', 'forte', 20, 1.1), (6, '28/01/2019', 'decaffeinato', 20, 0.93), (6, '28/01/2019', 'normale', 30, 1.1), (6, '28/01/2019', 'robusto', 50, 1.85), (6, '28/01/2019', 'lungo', 30, 1.2), (9, '29/01/2019', 'arabico', 40, 1.88), (5, '31/01/2019', 'ristretto', 10, 1.32), (5, '31/01/2019', 'arabico', 20, 1.76), (5, '31/01/2019', 'robusto', 30, 2.05), (5, '31/01/2019', 'lungo', 50, 1.2), (5, '31/01/2019', 'normale', 10, 1.1), (10, '04/02/2019', 'forte', 20, 1.07), (10, '04/02/2019', 'arabico', 50, 1.41), (10, '04/02/2019', 'robusto', 30, 2.12), (10, '04/02/2019', 'intenso', 30, 1.29), (20, '06/02/2019', 'robusto', 40, 1.78), (20, '06/02/2019', 'normale', 20, 0.84), (3, '06/02/2019', 'decaffeinato', 40, 1.12), (3, '06/02/2019', 'lungo', 50, 1.71), (19, '07/02/2019', 'normale', 30, 0.92), (19, '07/02/2019', 'arabico', 50, 1.95), (19, '07/02/2019', 'forte', 20, 1.41), (19, '07/02/2019', 'ristretto', 30, 1.8), (19, '07/02/2019', 'intenso', 10, 1.15), (1, '07/02/2019', 'arabico', 30, 2.0)]

## 1.A
#  Partendo dalla struttura dati riportata sopra, restituite un dizionario come nell'esempio seguente
#   {
#   tipo_capsula1:[totale_quantita1, incasso_totale1],
#   tipo_capsula2:[totale_quantita2, incasso_totale2],
#   ...,
#   }
#   Ogni coppia riporta informazioni sui dati di vendita di un tipo di capsula.
#   La chiave e' una stringa contenente il tipo di capsula (es., 'ristretto', 'arabico', ...).
#   Il valore associato alla chiave e' una lista formata da due valori, rispettivamente
#   * il totale delle capsule vendute
#   * la cifra totale incassata dalla vendita
#   Deve essere presente un'unica coppia chiave valore nel dizionario
#   per ogni tipo diverso di capsula.

# (5, '03/01/2019', 'lungo', 10, 1.41)

dic1A={}
for n in datiCapsule:
  if n[2] not in dic1A:
    dic1A[n[2]]=[n[3],n[4]]
  else:
    dic1A[n[2]][0]+=n[3]
    dic1A[n[2]][1]+=n[4]
print(dic1A)


## 1.B
#   Partendo dalla struttura dati riportata all'inizio, individuate i dati del "cliente mediano",
#   rispetto al totale delle capsule acquistate. Se ci fossero piu' clienti mediani possibili, sceglietene
#   uno come meglio preferite. Restituite la tupla seguente:
#      (id_cliente_mediano, totale_capsule_acquistate_dal_cliente_mediano)
#   I due valori all'interno della tupla devono essere entrambi interi.
#   Per calcolare il cliente mediano rispetto al totale delle capsule acquistate da ogni cliente dovete:
#   1) calcolare per ogni cliente il totale delle quantita' di capsule
#       acquistate (indipendentemente dalla tipologia).
#   2) Ordinare i totali in ordine crescente.
#   3) dovete recuperare l'id del cliente le cui quantita' occupano
#      il punto centrale della lista.
#      Data una lista li, la posizione centrale puo' essere calcolata con int(len(li)/2)

#Punto 1 calcolo per ogni cliente quante capsule ha acquistato
dic1B={}
for n in datiCapsule:
  if n[0] not in dic1B:
    dic1B[n[0]]=n[3]
  else:
    dic1B[n[0]]+=n[3]
print(dic1B)

#Punto 2 faccio una lista di tuple per ordinarle in ordine crescente

cllist=[]
for k, v in dic1B.items():
  cllist.append((k,v))

#funzione per ordinare in ordine crescente
def secondoElemento(elem):
  return elem[1]
cllist.sort(key=secondoElemento)
print(cllist)

#Punto 3 recupero posizione mediana e ID cliente posizione mediana
poscentrale=int(len(cllist)/2)
print(poscentrale)
idclientemediano=cllist[poscentrale][0]
print(idclientemediano)

#FINE

#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

# Esercizio 2.

# La seguente struttura dati memorizza le informazioni sui soldi caricati e spesi su macchinette distributrici di caffe', snack, etc.

# Nella seguente lista ogni tupla rappresenta un'operazione svolta da un cliente su una macchinetta.
# * il primo elemento della tupla corrisponde ad un valore numerico che identifica univocamente un cliente
# * il secondo e il terzo elemento della tupla corrispondono rispettivamente al tipo di operazione e all'importo dell'operazione effettuata:
#     - se il tipo di operazione e' uguale a 0 allora si tratta di una ricarica di soldi nella chiavetta e l'importo dell'operazione effettuata rappresenta l'importo caricato.
#     - se il tipo di operazione e' maggiore di 0, allora si tratta di un acquisto e il valore presente rappresenta l'identificatore del prodotto acquistato;
#       l'importo dell'operazione effettuata memorizza il costo del prodotto. L'importo dell'operazione effettuata è espressa in centesimi di euro.
#
# Ad esempio: la tupla (1, 0, 400) ci dice che il cliente 1 ha ricaricato 4 euro; la tupla (1, 29, 65) ci dice che il cliente 1 ha acquistato il prodotto 29 pagando 65 centesimi di euro.

datiMacchinette=[(1, 0, 400), (1, 29, 65), (1, 29, 65), (1, 29, 65), (1, 51, 100), (1, 51, 100), (1, 51, 100), (1, 51, 100), (3, 0, 200), (3, 16, 165), (3, 0, 300), (19, 0, 300), (13, 0, 300), (17, 0, 200), (17, 17, 20), (17, 12, 105), (17, 0, 100), (18, 0, 200), (6, 0, 100), (6, 18, 5), (6, 7, 50), (6, 0, 100), (6, 27, 120), (5, 0, 100), (5, 31, 60), (5, 0, 500), (0, 0, 100), (0, 0, 100), (0, 3, 170), (0, 0, 200), (0, 17, 110), (11, 0, 400), (8, 0, 200), (8, 36, 180), (8, 0, 500), (8, 16, 35), (4, 0, 500), (4, 31, 25), (14, 0, 400), (14, 15, 100), (14, 36, 140), (12, 0, 100), (9, 0, 100), (9, 14, 95), (9, 0, 500), (9, 6, 55), (9, 11, 85), (7, 0, 400), (7, 25, 125), (7, 22, 180), (7, 0, 200), (15, 0, 400), (15, 7, 185), (10, 0, 200), (10, 36, 70), (10, 0, 400)]


## 2.A
#   Partendo dalla struttura dati sopra riportata, restituite un valore intero corrispondente al totale incassato
#   con la vendita dei prodotti il cui prezzo di vendita e' compreso tra "1 euro e 50 centesimi" e "2 euro" (estremi esclusi).
totvendita=0
for n in datiMacchinette:
  if n[1]>0 and 150<=n[2]<=200:
    totvendita+=n[2]
print(str(totvendita/100) + "€")

## 2.B
#   Partendo dalla struttura dati sopra riportata, restituite un dizionario come nell'esempio seguente
#        {
#         id_cliente1:saldo_residuo1,
#         id_cliente2:saldo_residuo2,
#         ...,
#         id_clienteN:saldo_residuoN
#        }
#   Ogni coppia riporta informazioni sulla quantita' di denaro rimasta nella chiavetta del cliente (il saldo residuo)
#   dopo lo svolgimento delle operazioni.
#   Nella struttura dati restituita,
#   * id_cliente riporta l'identificatore del cliente,
#   * saldo_residuo riporta la somma rimasta nella chiavetta.
#   Tutte le chiavette hanno un credito iniziale
#   pari a 0 prima del primo utilizzo.

diccredit={}
for n in datiMacchinette:
  if n[1]==0:
    if n[0] in diccredit:
      diccredit[n[0]]+=n[2]
    else:
      diccredit[n[0]]=n[2]
print(diccredit)

dicspesa={}
for n in datiMacchinette:
  if n[1]>0:
    if n[0] in dicspesa:
      dicspesa[n[0]]+=n[2]
    else:
      dicspesa[n[0]]=n[2]
print(dicspesa)

dicsaldo={}
for k, v in diccredit.items():
  dicsaldo[k]=v
  if k in dicspesa:
    dicsaldo[k]-=dicspesa[k]
print(dicsaldo)

print("FINE ESERCIZIO 2C")


## 2.C
#   Partendo dalla struttura dati sopra riportata, restituite un dizionario come nell'esempio seguente
#        {
#          id_cliente1:[id_prodottoX, num_acquistiX],
#          id_cliente2:[id_prodottoY, num_acquistiY],
#          ...
#          id_clienteN:[id_prodottoZ, num_acquistiZ],
#        }
#   Ogni chiave del dizionario corrisponde all'id di un cliente che ha almeno effettuato
#   una ricarica o un'acquisto alle macchinette.
#   Ad ogni chiave deve essere associata una lista con due informazioni:
#   *  l'id del prodotto piu' acquistato dal cliente
#   *  il numero di volte in cui il prodotto
#      (del punto precedente) e' stato acquistato
#      dal cliente.
#   Alcune precisazioni che vi possono essere utili:
#   - Per vostra semplicita', ogni acquisto nelle  macchinette corrisponde
#     all'erogazione di un unico prodotto.
#   - Se piu' prodotti a pari merito risultano tra i piu' acquistati da un cliente,
#     sceglietene uno con un criterio a vostra scelta.
#   - se per un id_cliente non ci fossero vendite, inserire
#     * il valore -1 come id prodotto e
#     * il valore -1 come num_acquisti

dicAcquisti={}
for n in datiMacchinette:
  if n[0] not in dicAcquisti:
    dicAcquisti[n[0]]={}
    dicAcquisti[n[0]][n[1]]=1
  elif n[0] in dicAcquisti:
    if n[1] not in dicAcquisti[n[0]]:
      dicAcquisti[n[0]][n[1]]=1
    else:
      dicAcquisti[n[0]][n[1]]+=1

print(dicAcquisti)
print("Fine prima parte esercizio")
print("Fine prima parte esercizio")
print("Fine prima parte esercizio")

def second(elem):
  return elem[1]

dicRiass={}
for n in dicAcquisti:
  templist=[]
  for k,v in dicAcquisti[n].items():
    if k!=0:
      templist.append((k,v))
      templist.sort(key=second, reverse=True)
      dicRiass[n]=[k,v]
    elif n not in dicRiass:
      dicRiass[n]=[-1,-1]
  #print(templist)
for k,v in dicRiass.items():
  print(k,v)
print(dicRiass)