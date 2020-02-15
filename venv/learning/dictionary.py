items = {"latte": 3, "riso": 2, "tofu": 5}
print(items)

items["latte"] =2
print(items)

items["cereali"] = 1
print(items)

items["yogurt"] = {"fragola": 2, "bianco": 3}
print(items)

print(items["yogurt"]["fragola"])

print(items.keys())

keys = list(items.keys())
print(keys)

values = list(items.values())
print(values)