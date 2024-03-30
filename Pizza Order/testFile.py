from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_CustomPizza():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    cp1.addTopping("pepperoni")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ sausage\n\t+ pepperoni\nPrice: $15.00\n"

def test_SpecialtyPizza():
    sp = SpecialtyPizza("L", "Carne-more")
    assert sp.getPizzaDetails() == "SPECIALTY PIZZA\nSize: L\nName: Carne-more\nPrice: $16.00\n"

def test_PizzaOrder():
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

def test_OrderQueue():
    order1 = PizzaOrder(120000)
    order2 = PizzaOrder(124500)
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    queue = OrderQueue()
    queue.addOrder(order1)
    queue.addOrder(order2)
    assert queue.processNextOrder() == \
"******\n\
Order Time: 120000\n\
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
    
    assert queue.processNextOrder() == \
"******\n\
Order Time: 124500\n\
TOTAL ORDER PRICE: $0.00\n\
******\n"
    
test_CustomPizza()
test_SpecialtyPizza()
test_PizzaOrder()
test_OrderQueue()