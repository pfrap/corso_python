"""Media, numerosità predeterminata
Scrivete un programma python che calcola la media di un insieme di numeri immessi da tastiera. Il programma deve richiedere le
dimensioni dell'insieme (cioè di quanti numeri dovrà essere calcolata la media) in anticipo, cioè prima di richiedere a tastiera i
singoli valori. Stampate a video il valore della media. Per risolvere l'esercizio si suggerisce di introdurre un contatore per tenere
conto del numero di valori inseriti."""

"""
insieme=int(input("Di quanti numeri e' composto insieme?"))
listanumeri=[]
for n in range(insieme):
    listanumeri.append(int(input("Inserisci numero")))
media=sum(listanumeri)/insieme
print(media)
print(listanumeri)"""

"""Media, numerosità non determinata a priori
Scrivete un programma python che calcola la media di un insieme di numeri immessi da tastiera. A differenza dell'esercizio
precedente, il programma non deve richiedere inizialmente la quantità di numeri da inserire, ma deve iniziare subito a richiedere i
numeri dei quali deve calcolare la media. Quando la sequenza di numeri termina, l'utente inserisce uno zero come segnale che
la sequenza di numeri è finita. Il programma dovrà stampare a video quanti numeri sono stati inseriti e la loro media."""
"""
i=1
lista=[]
while i!=0:
    x=int(input("Inserisci numero"))
    lista.append(x)
    if x==0:
        i=0
print("Hai inserito %d numeri" %(len(lista)))
print("La loro media è {}".format(sum(lista)/len(lista)))"""

"""Medie in contemporanea
Scrivete un programma che richiede in input 5 numeri e calcola:
la media dei numeri positivi (>=0)
la media dei numeri negativi (<0)
Le due medie devono essere visualizzate a video. Nota: i 5 numeri non devono essere richiesti una seconda volta per calcolare
la seconda delle due medie. Stampa le due medie. Suggerimento: utilizzate i contatori
"""
"""lista=[]
for n in range(5):
    lista.append(int(input("Inserisci numero")))
listanegativi=[]
listapositivi=[]
for n in lista:
    if n<0:
        listanegativi.append(n)
    else:
        listapositivi.append(n)
print(listanegativi)
print("Media negativi è {}".format(sum(listanegativi)/len(listanegativi)))
print(listapositivi)
print("Media positivi è {}".format(sum(listapositivi)/len(listapositivi)))
"""

"""Medie in contemporanea con valori nulli
Come l'esercizio precedente, tuttavia considerate anche il caso in cui non sia possibile calcolare una delle due medie (es. si
sono inseriti solo numeri positivi o solo numeri negativi)."""

"""lista=[]
for n in range(5):
    lista.append(int(input("Inserisci numero")))
listanegativi=[]
listapositivi=[]
for n in lista:
    if n<0:
        listanegativi.append(n)
    else:
        listapositivi.append(n)
print(listanegativi)
if len(listanegativi)!=0:
    print("Media negativi è {}".format(sum(listanegativi)/len(listanegativi)))
print(listapositivi)
if len(listapositivi)!=0:
    print("Media positivi è {}".format(sum(listapositivi)/len(listapositivi)))
 """

"""Sequenza di Fibonacci
Scrivete un programma che calcoli i primi 20 numeri della sequenza di Fibonacci. La sequenza di Fibonacci è una sequenza di
numeri che inizia con i numeri 0 ed 1 e ogni numero successivo è la somma dei due numeri precedenti. Un esempio della
sequenza di Fibonacci è: 0 1 1 2 3 5 8 13 21 …"""

"""def sumFib(lung):
    fib=[]
    i=0
    k=1
    while i<lung:
        while i<2:
            fib.append(0)
            fib.append(1)
            i+=2
        fib.append(fib[k]+fib[k-1])
        k+=1
        i+=1
    print("Questa è la lista dei numeri di Fibonacci:{}".format(fib))
    print("Questa lista è lunga {} numeri".format(len(fib)))
    print("La loro somma è {}".format(sum(fib)))
    return (sum(fib))
sumFib(30)"""
"""
import random
number=random.randint(0,100)
i=False
while i==False:
    x=int(input("Inserisci un numero"))
    if x==number:
        i=True
        print("Hai trovato il numero")
    elif x>number:
        print("Numero troppo grande. Ritenta")
    elif x<number:
        print("Numero troppo piccolo. Ritenta")"""

"""Scrivete un programma che stampi a video la tabellina della moltiplicazione, dei numeri compresi tra 1 e 10.
Il programma dovrebbe produrre un output simile al seguente:
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
Il programma deve utilizzare due cicli annidati (il ciclo più interno deve stampare i singoli numeri di una riga, il ciclo più esterno
deve ripetere l'operazione di stampa per più righe). Consigli: nel comando print aggiungete una virgola finale, come nell'esempio:
print ( …), in questo modo l'output della print successiva sarà stampato sulla stessa riga senza andare a capo."""

"""
for x in range(1,20):
    for n in range(1,20):
        print(n*x, end=" ")
    print("\n")
"""
"""
Conta i numeri
Scrivete un programma python che calcola quanti numeri pari e quanti dispari sono presenti in un insieme di numeri immessi da
tastiera. Il programma deve richiedere le dimensioni dell'insieme (cioè di quanti numeri dovrà essere composto) in anticipo, cioè
prima di richiedere a tastiera i singoli valori. Stampate a video i due sotto-insiemi (quanti pari e quanti dispari) e la loro somma."""
"""
lista=[]
sizelist=int(input("Quanti numeri vuoi valutare?"))
for n in range(sizelist):
    x=int(input("Inserisci un numero"))
    lista.append(x)
pari=[]
dispari=[]
for n in lista:
    if n%2==0:
        pari.append(n)
    else:
        dispari.append(n)
print(pari)
print(dispari)
"""
"""
Maggiore e minore
Scrivete un programma che a partire da una lista contenente 10 numeri già inseriti, cerca il minore ed il maggiore tra i numeri
presenti. Per comodità potete copiare ed incollare nel vostro programma il seguente comando:
li=[30, 18, 54, 90, 6, 150, 114, 162, 72, 78]"""
"""
li=[30, 18, 54, 90, 6, 150, 114, 162, 72, 78]

y=0
x=0
i=False
k=li[0]
while i==False:
    x=k
    y=k
    i=True
for n in li:
    if n<x:
        x=n
    if n>y:
        y=n
print("Il numero minore è {}".format(x))
print("Il numero maggiore è {}".format(y))"""


"""
Controllo divisori
Scrivete un programma che crea due liste con 10 numeri interi l’una (scegliete voi se inserire i numeri da tastiera oppure
inizializzare le liste con dei numeri direttamente dentro il programma). Il programma dovrà costruire una (terza) lista di dieci valori
booleani, ognuno di questi dirà se il corrispondente elemento della seconda lista è un divisore intero del corrispondente elemento
della prima lista (cioè se il resto della divisione dei due elementi è nullo). Il programma dovrà stampare poi le tre liste."""

"""lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[2,4,6,8,10,12,14,16,18,20]
lista2a=[20,18,16,14,12,10,8,6,4,2]
lista3=[]
for n in range(len(lista1)):
    if lista1[n]%lista2a[n]==0:
        lista3.append(lista2a[n])
print(lista3)
"""

"""
Dati su tuple
Scrivete un programma che richiede il cognome, il nome e l’età di una persona. Queste informazioni devono essere memorizzate
in una tupla, la quale sarà aggiunta in coda ad una lista. Il programma dovrà ripetere l’operazione di inserimento delle
informazioni per 4 persone. Alla fine dell’inserimento il programma dovrà mostrare i dati delle persone che hanno "Rossi" come
cognome."""

"""lista=[]
for n in range(4):
    nome=str(input("Nome "))
    cognome=str(input("Cognome "))
    eta=int(input("Eta' "))
    tupla=(nome,cognome,eta)
    lista.append(tupla)
print(lista)
for n in lista:
    if n[1]=="rossi":
        print(n)
"""
"""
Multipli
Scrivete uno script che richiede all'utente di inserire un numero da tastiera maggiore di 2. Non occorre verificare che l'utente
abbia inserito un numero corretto. Lo script dovrà visualizzare a video tutti i multipli del numero 7 oppure del numero 9 compresi
tra 2 e il numero inserito dall'utente."""

"""num=int(input("Inserisci numero maggiore di due "))
i=3
k=1
while 2<i<num:
    i=7*k
    k+=1
    if i>num:
        k=1
        i=3
        break
    print(i, end=" ")
print("\n")
while 2<i<num:
    i=9*k
    k+=1
    if i>num:
        k=1
        i=3
        break
    print(i, end=" ")"""

"""
Divisori
Scrivete uno script che accetta in ingresso due numeri e 
identifica tutti i divisori in comune."""
"""
from matplotlib import pyplot as plt
import numpy as np

lista1=[]
lista2=[]
lista3=[]
for n in range(1,100):
    x=1/n
    lista1.append(x)
    lista2.append(n)
    lista3.append(x**2)

fig,ax=plt.subplots()
ax.plot(lista1, lista3, label="Funzione 3")
ax.plot(lista1, lista2, label="Funzione 2")
plt.title("Grafico di prova")
plt.legend()
fig.savefig("Prova3.pdf")
plt.show()
"""

"""
Somma
Calcolate la somma di tutti i numeri compresi tra 1 e un limite superiore fornito dall'utente a tastiera. Nell'eseguire il calcolo, NON
utilizzate la formula di Gauss, ma utilizzate contatori e cicli."""
"""
limite=int(input("Inserisci numero limite"))
somma=0
for n in range(0,limite):
	somma+=n
print(somma)

somma2=0
i=0
while i<=limite:
	somma2+=i
	i+=1
print(somma2)
"""

"""Le funzioni per generare dei numeri casuali dovrebbero avere una distribuzione uniforme. Vi chiediamo per un numero elevato di
volte di generare numeri casuali compresi tra 1 e 3 (estremi compresi) e di contare quante volte viene generato l'1, quante volte
il 2 e quante il 3. Visualizzate a video le numerosità dei numeri, la media e gli scostamenti in percentuale rispetto alla media.
Provate ad eseguire lo script diverse volte, ogni volta aumentando la quantità di numeri generati casualmente.
"""

"""
from random import randint
#Inserisco numero limite per definire quante volte generare un numero casuale

limite=int(input("Inserisci numero limite"))
lista=[]
for n in range(0,limite):
	x=randint(1,3)
	lista.append(x)

def numerosita(numero, lista):
	'''Funzione che calcola la numerosita 
	di un numero in una data lista'''
	count=0
	for n in lista:
		if n==numero:
			count+=1
	return count
	
def sommasingola(numero, lista):
	'''Funzione che calcola la somma di 
	un dato numero allinterno di una data lista.'''
	sommasing=0
	for n in lista:
		if n==numero:
			sommasing+=numero
	return sommasing
	
def calcolamedia(numero, lista):
	'''Funzione che restituisce in che percentuale 
	e presente un dato numero all interno di una lista'''
	count=0
	for n in lista:
		if n==numero:
			count+=1
	media=str(int(count/len(lista)*100))+"%"
	return media

#Calcolo la media di tutti i numeri della lista che servira' per gli scostamenti
sommatotale=0
for n in lista:
	sommatotale+=n
mediatotale=sommatotale/len(lista)
print(lista)
print("Nella lista sono presenti {} numeri".format(len(lista)))
print("La media della lista è {}".format(mediatotale))

print("****** ******")

print("Il numero 1 è presente {} volte".format(numerosita(1,lista)))
print("Rappresenta il {} del totale".format(calcolamedia(1,lista)))
print("Rispetto alla media si discosta di {}".format(1-mediatotale))
print("Il numero 2 è presente {} volte".format(numerosita(2,lista)))
print("Rappresenta il {} del totale".format(calcolamedia(2,lista)))
print("Rispetto alla media si discosta di {}".format(2-mediatotale))
print("Il numero 3 è presente {} volte".format(numerosita(3,lista)))
print("Rappresenta il {} del totale".format(calcolamedia(3,lista)))
print("Rispetto alla media si discosta di {}".format(3-mediatotale))
"""

"""TRIANGOLO DI FLOYD"""

"""
limite=int(input("Inserisci numero righe del Triangolo di Floyd "))
num=1
for n in range(0,limite):
	i=0
	while i<n:
		print(num, end=" ")
		i+=1
		num+=1
	print("\n")
"""