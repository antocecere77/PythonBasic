cat = "Elan"
age = 2
weight=5.678

#Error: can only concatenate str (not "int") to str
#print("Il mio gatto si chiama " + cat + "ed ha " + age + " anni")

#Formattazione (old school)
print("Il mio gatto si chiama %s ed ha %d anni e pesa %.2f" %(cat, age, weight))

#Formattazione (new school)
print("Il mio gatto si chiama {cat}, ed ha {age} anni e pesa {weight} kg".format(cat=cat, age=age, weight=weight))

#Formattazione Python 3.6
print(f"Il mio gatto si chiama {cat}, ed ha {age} anni e pesa {weight} kg")

