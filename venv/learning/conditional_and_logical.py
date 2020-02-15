#Operatori logici
print(1==4 and 2==2)
print(1==1 or 2==1)
print(not 1==1)

n = int(input("Inserisci un numero positivo: "))

if(n<0):
    print("%d non è un numero positivo" %n)
if(n%2==0):
    print("%d è un numero pari" %n)
else:
    print("%d è un numero dispari" % n)