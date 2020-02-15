#swapping (old school)
a = "cane"
b = "gatto"

tmp = a;
a = b
b = tmp

#swapping (new school)
a = "cane"
b = "gatto"
a,b = b,a

print(a, b)

n = int(input("Fino a che numero vuoi stampare?"))

for i in range(n):
    print(i)

#Fibonacci
n = int(input("Quanti numeri di Fibonacci vuoi stampare?"))
fib_num = 0;
next_fib_num = 1

for i in range(n):
    fib_num, next_fib_num = next_fib_num, next_fib_num+fib_num
    print("%d° numero di Fibonacci = %d"%(i+1, fib_num))

#Iterazione sulle liste
shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]
for i  in range(len(shopping_list)):
    print("%d) %s" % (i+1, shopping_list[i]))

for entry in shopping_list:
    print("-%s" % entry)

for i, entry in enumerate(shopping_list):
    print("%d) %s" % (i + 1, shopping_list[i]))