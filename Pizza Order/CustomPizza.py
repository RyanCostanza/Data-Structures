from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            self.setPrice(8.00)
        elif self.size == "M":
            self.setPrice(10.00)
        elif self.size == "L":
            self.setPrice(12.00)

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.setPrice(self.getPrice() + 0.50) 
        elif self.size == "M":
            self.setPrice(self.getPrice() + 0.75)
        elif self.size == "L":
            self.setPrice(self.getPrice() + 1.00)

    def getPizzaDetails(self):
        pizza = "CUSTOM PIZZA\n"
        pizza += "Size: {}\n".format(self.size)
        pizza += "Toppings:\n"
        for i in self.toppings:
                pizza += f"\t+ {i}\n"
        pizza += f"Price: ${self.getPrice():.2f}\n"
        return pizza
    
cp1 = CustomPizza("S")
assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

cp1 = CustomPizza("L")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"