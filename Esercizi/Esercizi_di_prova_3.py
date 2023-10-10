## ESERCIZI SU DATA E ORA
"""
from datetime import date, time

today= date.today()
print(type(today))
agne_birthday=date(2019,9,12)
edo_birthday=date(2023,2,10)
my_birthday=date(1990,4,27)
print(my_birthday)
print(my_birthday.day)
print(my_birthday.month)
print(my_birthday.year)

print(edo_birthday)
print(edo_birthday-my_birthday)
print(my_birthday.strftime("%A %d %m %Y"))
next_birthday=my_birthday.replace(year=my_birthday.year+33)
print(next_birthday.strftime("%A %d %m %Y"))
print("\n")

listagiorni=[]
for n in range(1,34):
	next_birthday= my_birthday.replace(year=my_birthday.year+n)
	print(next_birthday.strftime("%A, %d %m %Y"))
	listagiorni.append(next_birthday.strftime("%A"))
	
print(set(listagiorni))
print(agne_birthday-my_birthday)
differenza_edo=edo_birthday-my_birthday
print(edo_birthday-my_birthday)
print(type(differenza_edo))


## RIPARTO CON ALCUNI ESERCIZI
#Per importare il modulo data
from datetime import date
dataprova=date(2021,1,1) #Metodo standard per costruire delle date anno, mese, giorno
print("-"*30)
k="2022/01/01"
print(k)

k=k.replace("/", "-") #Sostituisco per portare data in formato iso
k=date.fromisoformat(k) #Da stringa formato iso costruisco data
print(k)
n="2023-01-01"
n=date.fromisoformat(n)
print(n)
print("-"*30)

diff=n-k #Se faccio la differenza mi da un formato timedelta
print(diff)
print(diff.days) #Formato timedelta puo avere metodo .days per riportare il delta in giorni
print(diff.total_seconds()/60/60) #Puo' avere metodo .total_seconds per portare differeza in secondi
lista=[]
print(dir(lista))
"""

from datetime import date, time, datetime

#papa=date(1990,4,27)
papa=date.fromisoformat("1990-04-27")
mamma=date(1992,9,12)
agne=date(2019,9,11)
edo=date(2023,2,10)


listaComple=[papa, mamma, agne, edo]
for n in listaComple:
	diff=n-papa
	print(diff.total_seconds()/60/60)

print(agne.strftime("%d %m %y"))
print(agne.strftime("%I:%M %p"))
print("-"*30)
ora=time(16, 5, 40)
ora2=time.fromisoformat("15:35:00")
print(ora)
print(type(ora))
print(ora2)
print(type(ora2))
print("-"*30)
delta=ora2-ora
print(delta)