def compute_area(b, h):
    area = b*h/2
    return area

b = 5
h = 3
print(compute_area(b, h))

def print_shopping_list(shopping_list, owner="Antonio"):
    print("La lista della spesa di %s" %owner)
    for i,entry in enumerate(shopping_list):
        print("%d) %s" %(i+1, entry))

shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]
print_shopping_list(shopping_list)
print_shopping_list(shopping_list, "Giuseppe")