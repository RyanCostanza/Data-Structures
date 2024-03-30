from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if size == "S":
            self.price = 12.00
        elif size == "M":
            self.price = 14.00
        elif size == "L":
            self.price = 16.00

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.getPrice():.2f}\n"

sp1 = SpecialtyPizza("S", "Carne-more")
assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"