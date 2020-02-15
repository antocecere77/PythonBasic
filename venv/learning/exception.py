num = input("Inserisci un numero:")
try:
    type(num)
    num = int(num)
    print("Il numero inserito è",num)
except ValueError:
    print("Il dato che hai inserito non è un numero")