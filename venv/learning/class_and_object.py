class Triangle:

    """
    Questa classe rappresenta un triagolo
    """
    def __init__(self, a,b,c,h):
        self.a, self.b, self.c, self.h = a,b,c,h

    def area(self) :
        """
        Calcolo dell'area del triangolo
        """
        return self.b*self.h/2

    def perimeter(self):
        """
        Calcolo del perimetro del triangolo
        """
        return self.a+self.b+self.c

    def print_info(self):
        print("Area del triangolo = %.2f"% self.area())
        print("Perimetro del triangolo = %.2f" % self.perimeter())

triangle = Triangle(4,3,8,3)

print(triangle.area())
print(triangle.perimeter())

triangle.print_info()

help(triangle)