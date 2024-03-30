from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def testInventory():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)
    bst.removeCar("BMW", "X5", 2022, 60000)
    
    assert bst.inOrder() == 'Make: AUDI, Model: A3, Year: 2021, Price: $25000' + '\n' + 'Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000' + '\n' + 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000' + '\n'

    pst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    pst.addCar(car1)
    pst.addCar(car2)
    pst.addCar(car3)
    pst.addCar(car4)
    pst.addCar(car5)

    pst.removeCar("BMW", "X5", 2020, 58000)
    pst.removeCar("BMW", "X5", 2022, 60000)
    assert pst.preOrder() == 'Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000' + '\n' + 'Make: AUDI, Model: A3, Year: 2021, Price: $25000' + '\n' + 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000' + '\n'

    hst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    hst.addCar(car1)
    hst.addCar(car2)
    hst.addCar(car3)
    hst.addCar(car4)
    hst.addCar(car5)

    hst.removeCar("BMW", "X5", 2020, 58000)
    hst.removeCar("BMW", "X5", 2022, 60000)
    assert hst.postOrder() == 'Make: AUDI, Model: A3, Year: 2021, Price: $25000' + '\n' + 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000' + '\n' + 'Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000' + '\n'
    


testInventory()