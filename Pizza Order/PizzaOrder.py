from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        order = ""
        order += "******\n"
        order += f"Order Time: {self.time}\n"
        for i in self.pizzas:
            order += i.getPizzaDetails()
            order += "\n----\n"
        sum = 0
        for i in self.pizzas:
            sum += i.getPrice()
        order += f"TOTAL ORDER PRICE: ${sum:.2f}\n"
        order += "******\n"
        return order
    
cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000)
order.addPizza(cp1)
order.addPizza(sp1)
assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"