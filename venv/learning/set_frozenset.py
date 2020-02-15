#Set
names = {"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"}
print(names)

#Aggiunta di un elemento
names.add("Lorenzo")
print(names)

#Rimuovere un elemento
names.remove("Antonino")
print(names)

#Errore perchè non esiste si usa discard se non siamo sicuri che esista
#names.remove("Paolo")
names.discard("Paolo")
print(names)

name = names.pop()
print(name)
print(names)

names.clear()
print(names)

#da lista a set
names_list = ["Giuseppe", "Federico", "Antonino", "Matteo", "Federico"]
print(names_list)

name_set = set(names_list)
print(name_set)

#da set a lista
names_list = list(name_set)
print(names_list)

#frozenset - set immutabili

names = frozenset({"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"})
