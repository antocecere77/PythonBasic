#Espressioni booleane

#uguaglianza
print(5==5)

#disuguaglianza
print("casa"!="g")

#maggioranza
print(6>9)
print(6>=6)

#minoranza
print(6<9)
print(6<=9)

#ciclo while
n = int(input("Fino a che numero vuoi contare? "))

i = 1
while i<n:
    if(i>=25):
        break
    if(i%3==0):
        i+=2
        continue
    print(i)
    i+=2