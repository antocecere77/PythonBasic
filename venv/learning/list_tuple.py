#Liste
my_list = [10, 5, 8, 3, 11, 2]
type(my_list)
len(my_list)

#indexing
my_list[0]
my_list[1]
my_list[2]

#slicing
print(my_list[0:3])    #10, 5, 8
print(my_list[:5])     #10, 5, 8, 3, 11
print(my_list[2:])     #8, 3, 11, 2
print(my_list[::-1])   #2, 11, 3, 8, 5, 10

#modifica
my_list[0] = 0
print(my_list)

my_list[-2:] = [7, 1]
print(my_list)

#verifica
animals = ["cane","gatto","topo"]
print("uomo" in animals)
print("gatto" in animals)

#rimozione per valore
animals.remove("gatto")
print(animals)

#estrazione per valore
animal = animals.pop(1)
print(animals)
print(animal)

#aggiunta di elementi
animals.append("bestia demoniaca")
print(animals)

#inserimento di elementi
animals.insert(1, "topo")
print(animals)

#Tuple (simile alla lista ma non modificabile)
my_tuple = (10, 5.5, "ciao", "ciao")
type(my_tuple)
print(my_tuple)

print(my_tuple[1])
print(my_tuple[:3])

#Error
#my_tuple[0] = 0 #'tuple' object does not support item assignment

#ottenere l'indice di un elemento
print(my_tuple.index("ciao"))

#conta gli elementi
print(my_tuple.count("ciao"))

#lunghezza di una tupla
print(len(my_tuple))

hello = "hello python"
print(len(hello))
