# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'flottaAuto'

# Vi forniamo un esempio di struttura dati che potrebbe
# essere restituita da una delle funzioni seguenti.
# La (vera) struttura dati caricata dal file sara' diversa:
# può essere più lunga, i primi elementi possono differire come valori.

datiFlotta=[('G1', 'VU120TM', 10, 90), ('G1', 'ML147OE', 45, 359), ('G1', 'WQ616LH', 40, 518), ('G1', 'JT776XI', 5, 55), ('G1', 'GC237KT', 5, 31), ('G1', 'QZ499GB', 15, 117), ('G1', 'EK274HV', 45, 403), ('G2', 'NI744BS', 20, 154), ('G2', 'GC237KT', 10, 65), ('G2', 'EP016HP', 40, 598), ('G2', 'KF234TQ', 30, 185), ('G2', 'GM127CC', 5, 79), ('G2', 'EN065TU', 15, 248), ('G2', 'RJ530VN', 20, 360), ('G2', 'PD452QD', 20, 218), ('G2', 'QA408MW', 10, 81), ('G2', 'GV183BX', 40, 475), ('G3', 'GM127CC', 30, 552), ('G3', 'JT776XI', 5, 46), ('G3', 'RJ530VN', 5, 89), ('G3', 'EV599RN', 25, 120), ('G3', 'EP016HP', 20, 234), ('G3', 'NJ637QS', 10, 135), ('G3', 'BA867OR', 5, 64), ('G3', 'VU120TM', 15, 124), ('G3', 'OH062GK', 25, 141), ('G3', 'HN165WY', 35, 450), ('G3', 'NB994MY', 25, 403), ('G4', 'PD470UJ', 35, 504), ('G4', 'BA867OR', 50, 742), ('G4', 'EK274HV', 20, 177), ('G4', 'ML147OE', 25, 169), ('G4', 'EP016HP', 20, 286), ('G4', 'WQ616LH', 15, 266), ('G4', 'EN065TU', 20, 302), ('G4', 'GM127CC', 10, 152), ('G4', 'KF234TQ', 35, 239), ('G4', 'GG666VN', 5, 111), ('G4', 'JN795IR', 30, 344), ('G5', 'GC237KT', 20, 120), ('G5', 'RJ530VN', 25, 454), ('G5', 'DI052KU', 35, 407), ('G5', 'BA867OR', 20, 297), ('G5', 'QZ499GB', 25, 145), ('G6', 'EV599RN', 40, 199), ('G6', 'EK274HV', 15, 141), ('G7', 'OH062GK', 5, 30), ('G7', 'DI052KU', 40, 547), ('G7', 'PD470UJ', 40, 672), ('G7', 'EN065TU', 15, 264), ('G7', 'GG666VN', 15, 336), ('G7', 'SN351FS', 50, 950), ('G7', 'VF541LZ', 20, 180), ('G7', 'EK274HV', 10, 65), ('G7', 'GM127CC', 5, 94), ('G8', 'GG666VN', 35, 764), ('G8', 'EP016HP', 35, 368), ('G8', 'QZ499GB', 25, 206), ('G8', 'CY009LW', 35, 148), ('G8', 'RJ530VN', 50, 720), ('G8', 'NB994MY', 50, 1007), ('G8', 'OH062GK', 15, 97), ('G8', 'NJ637QS', 40, 632), ('G9', 'EN065TU', 45, 834), ('G9', 'NI744BS', 25, 192), ('G9', 'GC237KT', 10, 67), ('G9', 'BA867OR', 20, 354), ('G9', 'VF541LZ', 50, 500), ('G9', 'WQ616LH', 40, 608), ('G9', 'CY009LW', 15, 78), ('G9', 'GG666VN', 20, 444), ('G9', 'SN351FS', 40, 912), ('G9', 'QA408MW', 45, 517), ('G9', 'EV599RN', 5, 28), ('G10', 'EV599RN', 15, 104), ('G10', 'EN065TU', 30, 621), ('G10', 'GM127CC', 50, 896), ('G10', 'PD470UJ', 40, 522),]


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py (o un notebook equivalente)
# da compilare e un file dati, descritto qua di seguito.
#
# - File 1) 'consumiFlotta.csv'
#   Il file memorizza le informazioni sulle auto utilizzate 
#   da un gruppo di guidatori, sui km percorsi e sui 
#   litri di carburante consumati.
#   Un esempio del contenuto del file e' contenuto nella stringa seguente
#   La prima riga descrive la struttura delle righe successive.
#   I valori sono separati da ; e per andare a capo e' usato il \n
"""
id_guidatore;targa1;litri1;km1;targa2;litri2;km2;...;targaN;litriN;kmN
G1;VU120TM;10L;90KM;ML147OE;45L;359KM;WQ616LH;40L;518KM;JT776XI;5L;55KM;GC237KT;5L;31KM;QZ499GB;15L;117KM;EK274HV;45L;403KM
G2;NI744BS;20L;154KM;GC237KT;10L;65KM;EP016HP;40L;598KM;KF234TQ;30L;185KM;GM127CC;5L;79KM;EN065TU;15L;248KM;RJ530VN;20L;360KM;PD452QD;20L;218KM;QA408MW;10L;81KM;GV183BX;40L;475KM
G3;GM127CC;30L;552KM;JT776XI;5L;46KM;RJ530VN;5L;89KM;EV599RN;25L;120KM;EP016HP;20L;234KM;NJ637QS;10L;135KM;BA867OR;5L;64KM;VU120TM;15L;124KM;OH062GK;25L;141KM;HN165WY;35L;450KM;NB994MY;25L;403KM
G4;PD470UJ;35L;504KM;BA867OR;50L;742KM;EK274HV;20L;177KM;ML147OE;25L;169KM;EP016HP;20L;286KM;WQ616LH;15L;266KM;EN065TU;20L;302KM;GM127CC;10L;152KM;KF234TQ;35L;239KM;GG666VN;5L;111KM;JN795IR;30L;344KM
G5;GC237KT;20L;120KM;RJ530VN;25L;454KM;DI052KU;35L;407KM;BA867OR;20L;297KM;QZ499GB;25L;145KM
G6;EV599RN;40L;199KM;EK274HV;15L;141KM
...
"""
#   In ogni record (record e' un sinonimo di 'riga')
#   sono memorizzate le auto guidate da un guidatore, i litri consumati ed i 
#   km percorsi. Attenzione, quando un guidatore guida diversi veicoli,
#   su una riga ci possono essere i dati di piu' veicoli.
#   Le informazioni sono organizzate nel modo seguente. 
#   - id_guidatore. E' sempre la prima informazione della riga. 
#     Si tratta di una stringa che inizia con 'G' e che identifica
#     univocamente un guidatore.
#   - targa. Per esempio AA123BB, è la targa dell'automezzo guidato. 
#   - litri. Sono i litri di carburante consumati dall'autista alla guida 
#     dell'auto la cui targa si trova a sinistra di litri.
#   - km percorsi. I km percorsi dall'autista con il veicolo.
#   - ... 
#     se nella riga sono presenti i dati di piu' veicoli, 
#     per ogni veicolo sono riportati (sempre nello stesso ordine)
#     targa, litri, e km percorsi. Litri e km si possono 
#     riconoscere oltre che dall'ordine, anche dalla/e lettere finali, 
#     rispettivamente L e KM.
#   
#   Alcune note sul contenuto del file
#   - Il numero dei dati presente in ogni riga cambia in base 
#     al numero di veicoli guidati dal guidatore.
#   - Lo stesso veicolo puo' essere guidato da guidatori diversi,
#     pertanto la targa di un veicolo puo' apparire in molte righe.
#     Tuttavia, i dati presenti in una riga fanno riferimento solo 
#     ai litri consumati e ai km percorsi dal guidatore 
#     di riferimento della riga.
#   - In una riga, una stessa targa non puo' essere presente piu' di 
#     una volta.
#
#   ***NOTA BENE***: aprite il file .csv
#     - con un editor di testo diverso da notepad 
#     - senza usare excel (o programmi similari)

##########################################################
# INTRODUZIONE AL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà in dettaglio che cosa fare.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete, potete implementare funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente, caricaDatiFlotta(), accetta come parametro in ingresso
#   il nome del file .csv contenente i dati descritti in precedenza.
#   La funzione deve leggere il contenuto del file e
#   restituire una lista di tuple, come nell'esempio seguente:
#        [
#          ('id_guidatore1', 'targa_automezzo1', litri, km_percorsi),
#          ('id_guidatore1', 'targa_automezzo2', litri, km_percorsi),
#          ('id_guidatore2', 'targa_automezzo5', litri, km_percorsi),
#          ('id_guidatore2', 'targa_automezzo6', litri, km_percorsi),
#          ...
#        ]
#   dove ogni tupla contiene le informazioni su litri e km percorsi
#   da un autista su un automezzo. 
#   Per esempio, la funzione applicata ad un file con il contenuto seguente
"""id_guidatore;targa1;litri1;km1;targa2;litri2;km2;...;targaN;litriN;kmN
G1;VU120TM;10L;90KM;ML147OE;45L;359KM;WQ616LH;40L;518KM
G2;NI744BS;20L;154KM
...
"""
#   deve restituire una struttura dati come la seguente
#   [ 
#     ('G1','VU120TM',10,90), # gli ultimi due valori sono rispettivamente i litri e i chilometri percorsi
#     ('G1','ML147OE',45,359),
#     ('G1','WQ616LH',40,518), # qui finiscono i dati della prima riga
#     ('G2','NI744BS',20,154),
#     ...
#   ]
#   In ogni tupla, litri e km percorsi devono essere valori interi
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete lavorare sulle funzioni successive senza
#   implementare l'attuale, potete utilizzare la struttura dati dichiarata
#   all'inizio di questo script (basta togliere il commento dalla prima riga di codice).
#   In quest'ultimo caso tuttavia la funzione sara' considerata non svolta.
def caricaDatiFlotta(fn):
    # return datiFlotta # se non riuscite ad implementare la funzione, potete usare temporaneamente questa struttura dati
    # Implementa il codice della funzione qua sotto. La riga con il pass puo' essere cancellata.
    pass
    fd=open(fn, 'r')
    fd.readline() # salto la prima riga
    li=[]
    for line in fd:
        elemsLi=line.strip('\n').split(';')
        idGuidatore=elemsLi[0]
        ii=1
        while ii<len(elemsLi):
            targa=elemsLi[ii]
            litriSt=elemsLi[ii+1]
            litri=int(litriSt[:-1]) # escludo l'ultimo elemento
            kmSt=elemsLi[ii+2]
            km=int(kmSt[:-2]) # escludo gli ultimi due elementi
            li.append( (idGuidatore, targa, litri, km) )
            ii+=3
    return li
    
    

# - La funzione trovaPiedePesante() accetta come parametri in ingresso 
#   la struttura dati restituita dalla funzione caricaDatiFlotta().
#   La funzione trovaPiedePesante() deve restituire le informazioni sul 
#   guidatore che ha il valore piu' basso dell'indicatore
#   km_per_litro = (totale chilometri percorsi dal guidatore) / (totale dei litri consumati dal guidatore).
#   Precisazione: un automezzo puo' essere usato da piu' guidatori, tuttavia
#   nel calcolo dell'indicatore per un guidatore vanno considerati 
#   solo i km percorsi e il carburante da lui consumato.
#   Se ci fossero piu' guidatori a pari merito (con il valore piu' basso
#   dell'indicatore km_per_litro), sceglietene uno come meglio preferite.
#   La funzione deve restituire una tupla come la seguente
#   (id_guidatore, km_totali, litri_totali, km_per_litro)
#   con i dati del guidatore selezionato. 
#   km_totali rappresenta i km totali percorsi dal guidatore, 
#   litri_totali e' il totale dei litri consumati dal guidatore,
#   km_per_litro e' il rapporto tra i due valori precedenti e 
#      deve essere di tipo float.
def trovaPiedePesante(ds): 
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    diz={}
    for tu in ds:
        guidatore=tu[0]
        litri=tu[2]
        km=tu[3]
        if guidatore not in diz:
            diz[guidatore]=[0, 0] # litri, km
        diz[guidatore][0]+=litri
        diz[guidatore][1]+=km
    # calcolo ora il rapporto
    guid2rap={}
    for guid in diz:
        guid2rap[guid]=diz[guid][1] / float(diz[guid][0])

    #print(guid2rap)
    minGuid=list(guid2rap.keys())[0] # prendo la prima delle chiavi
    #minGuid=guid2rap.keys()[0] # Python2
    for guid in guid2rap:
        # se trovo una persona col piede piu' pesante, 
        # questa diventa il nuovo minGuid
        if guid2rap[guid]<guid2rap[minGuid]:
            minGuid=guid # 
    #(id_guidatore, km_totali, litri_totali, km_per_litro)
    tu=(minGuid, diz[minGuid][1], diz[minGuid][0], diz[minGuid][1] / float(diz[minGuid][0]))
    return tu
    

# - La funzione trovaAutomezzi() accetta come parametri in ingresso 
#   la struttura dati restituita dalla funzione caricaDatiFlotta().
#   La funzione trovaAutomezzi() deve individuare i 5 automezzi che hanno
#   hanno percorso piu' strada (considerando la strada percorsa da tutti
#   i guidatori). 
#   La funzione deve restituire una lista di 5 targhe, come 
#   nell'esempio seguente (i valori non coincidono con il risultato che 
#   dovrete ottenere) 
#      ['AA123BB', 'CC456DD', ... 'kk747JJ']
#   Le targhe devono essere ordinate, da sinistra verso destra 
#   in ordine decrescente di km percorsi. Se ci fossero 
#   automezzi con pari percorrenza, scegliete voi in che ordine disporli. 
#   In ogni caso, la lista restituita deve avere solo 5 elementi.
# - Facoltativo: non utilizzate le funzioni di ordinamento presenti 
#   in libreria ma implementate voi un algoritmo di orninamento. 
#   Facoltativo significa che non siete obbligati a farlo, ma se lo fate 
#   potreste prendere dei punti extra 
def trovaAuto(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    diz={}
    for tu in ds:
        targa=tu[1]
        km=tu[3]
        if targa in diz:
            diz[targa]+=km
        else:
            diz[targa]=km
    
    li = list(diz.keys()) # creo una lista di targhe

    # ordino le targhe in ordine decrescente di km
    # uso il bubble sort
    ordinato=False    
    while ordinato==False:
        ordinato=True
        ii=0
        while ii<len(li)-1:
            if diz[li[ii]] < diz[li[ii+1]]: # se le percorrenze non sono nell'ordine giusto
                #scambio le targhe
                temp=li[ii]
                li[ii]=li[ii+1]
                li[ii+1]=temp
                ordinato=False
            ii+=1
    
    return li[:5] # restituisco solo i primi 5 elementi della lista
    
"""Dario, io per sse mi fermerei qua, tuttavia si potrebbe aggiungere anche la seguente
funzione"""
    
# - La funzione seguente accetta come parametri in ingresso la struttura dati
#   restituita dalla funzione caricaDatiFlotta().
#   La funzione deve individuare l'automezzo che e' stato guidato da piu' persone
#   considerando tuttavia solo le persone che hanno guidato almeno 4 automezzi diversi.
#   La funzione deve restituire una stringa con la targa dell'automezzo che soddisfa 
#   i criteri appena descritti. Se ci fossero piu' automezzi a pari merito, 
#   sceglietene uno come meglio preferite.
def piuGuidato(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass
    #individuo per ogni guidatore l'elenco mezzi guidati
    diz={}
    for tu in ds:
        guidatore=tu[0]
        targa=tu[1]
        if guidatore in diz:
            if targa not in diz[guidatore]: # questo controllo non servirebbe
                diz[guidatore].append(targa)
        else:
            diz[guidatore]=[targa]
    
    # individuo i guidatori che hanno guidato almeno 4 mezzi
    liGuid=[]
    for guid in diz:
        if len(diz[guid]) >= 4:
            liGuid.append(guid)

    # adesso costruisco un dizionario che associa ad ogni automezzo il numero di guidatori, considerando solo i guidatori presenti in liGuid
    targa2numGuid={}
    for guid in diz:
        if guid in liGuid: # se e' tra i guidatori che hanno guidato 4 veicoli
            for targa in diz[guid]:
                if targa in targa2numGuid:
                    targa2numGuid[targa]+=1
                else:
                    targa2numGuid[targa]=1     
    
    #assumo temporaneamente che il risultato sia la prima
    print(targa2numGuid)
    maxTarga=list(targa2numGuid.keys())[0]
    for targa in targa2numGuid:
        if targa2numGuid[targa]>targa2numGuid[maxTarga]:
            maxTarga=targa

    # python3 e python3 productono risultati diversi perche' ci sono piu' targhe a pari merito
    return maxTarga



##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('-'*30)
print('Esercizio %s.' % (nomeEsercizio))
print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione caricaDatiFlotta: ')
csvfn = 'consumiFlotta.csv'
dflo = caricaDatiFlotta(csvfn)
print(dflo)

print('2) Eseguo la funzione trovaPiedePesante: ')
res2 = trovaPiedePesante(dflo)
print(res2)

print('3) Eseguo la funzione trovaAutomezzi: ')
res3 = trovaAuto(dflo)
print(res3)

print("4) Eseguo la funzione piuGuidato:  ")
res4 = piuGuidato(dflo)
print(res4)


print('Nome file e autore dello script eseguito')
# commentata l'istruzione qua sotto per problemi con jupyter, ... da ricontrollare
#print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
print('-'*30)
