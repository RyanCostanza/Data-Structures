from CarInventoryNode import CarInventoryNode
from Car import Car

class CarInventory:
    def __init__(self): 
        self.root = None
        self.size = 1
  
    def addCar(self,car):
        if self.root:
            self.addCarHelper(car,self.root)
        else:
            self.root = CarInventoryNode(car)
            self.size += 1
    
    def addCarHelper(self, car, cnode):
        if car.make == cnode.make and car.model == cnode.model:
            cnode.cars.append(car)
        elif car.make < cnode.make:
            if cnode.left:
                self.addCarHelper(car, cnode.left)  
            else:
                cnode.setLeft(CarInventoryNode(car))
                cnode.left.setParent(cnode)      
        elif car.make == cnode.make and car.model < cnode.model:
            if cnode.left:
                self.addCarHelper(car, cnode.left)  
            else:
                cnode.setLeft(CarInventoryNode(car))      
                cnode.left.setParent(cnode)      

        else:
            if cnode.right:
                self.addCarHelper(car, cnode.right)      
            else:
                cnode.setRight(CarInventoryNode(car))
                cnode.right.setParent(cnode)      

    def preOrder(self):
        return self.preOrderHelper(self.root)
    
    def preOrderHelper(self,current):
        result = ''
        if current:
            result += str(current)
            result += self.preOrderHelper(current.left)
            result += self.preOrderHelper(current.right)
        return result


    def inOrder(self):
        return self.inOrderHelper(self.root)
    
    def inOrderHelper(self, current):
        result = ''
        if current:
            result += self.inOrderHelper(current.left)
            result += str(current)
            result += self.inOrderHelper(current.right)
        return result


    def postOrder(self):
        return self.postOrderHelper(self.root)
    
    def postOrderHelper(self,current):
        result = ''
        if current:
            result += self.postOrderHelper(current.left)
            result += self.postOrderHelper(current.right)
            result += str(current)
        return result

    def doesCarExist(self, car):
        if self.root:
            r = self.doesCarExistHelper(car,self.root)
            if r:
                for i in r.cars:
                    if i == car:
                        return True
                return False
            else:
                return False
        else:
            return False

    def doesCarExistHelper(self, car, cnode):
        keyNode = CarInventoryNode(car)
        if cnode is None or cnode == keyNode:
            return cnode
        if cnode < keyNode:
            return self.doesCarExistHelper(car, cnode.right)
        return self.doesCarExistHelper(car, cnode.left)

    def getBestCar(self, make, model):
        r = self.getBestCarHelper(make, model, self.root)
        if r is not None:
            return max(r.cars)
        return None

    def getBestCarHelper(self, make, model, cnode):
        keyNode = CarInventoryNode(Car(make, model, 0, 0))
        if cnode is None or cnode == keyNode:
            return cnode
        if cnode > keyNode:
            return self.getBestCarHelper(make, model, cnode.left)
        return self.getBestCarHelper(make, model, cnode.right)

    def getWorstCar(self, make, model):
        if self.root:
            r = self.getWorstCarHelper(make, model, self.root)
            if r:
                return min(r.cars)
            else:
                return None     
        else:
            return None

    def getWorstCarHelper(self, make, model, cnode):
        keyNode = CarInventoryNode(Car(make, model, 0, 0))
        if cnode is None or cnode == keyNode:
            return cnode
        if cnode < keyNode:
            return self.getWorstCarHelper(make, model, cnode.right)
        return self.getWorstCarHelper(make, model, cnode.left)

  

    def getTotalInventoryPrice(self):
        sum = 0
        q = []
        if self.root is not None:
            q.append(self.root)
            while len(q) > 0:
                temp = q.pop(0)
                for i in temp.cars:
                    sum += i.price 
            if (temp.left is not None):
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
 
        return sum    
    
    def getMinimum(self, node):
        current = node
   
        while(current is not None):
            if current.left is None:
                break
            current = current.left
   
        return current
    
    def getSuccessor(self, make, model):
        n = self.getBestCarHelper(make, model, self.root)
        if n:
            if n.right is not None:
                return self.getMinimum(n.right)
     
            successor=None
         
            root=self.root
            while(root):
                if(root<n):
                    root=root.right
                elif(root>n):
                    successor=root
                    root=root.left
                else:
                    break
            return successor
        else:
            return None
 

    def removeCar(self, make, model, year, price):
        cnode = self.doesCarExistHelper(Car(make, model, year, price),self.root)
        if cnode:
            for car in cnode.cars:
                if car == Car(make, model, year, price):
                    cnode.cars.remove(car)
                    if cnode.cars == []:
                        if self.size == 1 and cnode == self.root:
                            self.root = None
                            self.size = self.size - 1
                            return True
                        self.removeCarHelper(cnode)
                        return True
                    self.size = self.size-1
                    return True
        else:
            return False
   
      

    def removeCarHelper(self, cnode):
        if cnode.isLeaf():
            if cnode.parent is not None:
                if cnode == cnode.parent.left:
                        cnode.parent.left = None
                else:
                        cnode.parent.right = None
            else:
                cnode = None
                self.root = None
                self = None

        elif cnode.hasBothChildren():
                
                successor = cnode.findSuccessor()
                successor.spliceOut()
                cnode.make = successor.make
                cnode.model = successor.model
                cnode.cars = successor.cars

        else:
                if cnode.hasLeftChild():
                        if cnode.isLeftChild():
                                cnode.left.parent = cnode.parent
                                cnode.parent.left = cnode.left
                        elif cnode.isRightChild():
                                cnode.left.parent = cnode.parent
                                cnode.parent.right = cnode.left
                        else: 
                                cnode.replaceNodeData(cnode.left.make,
                                                            cnode.left.model,
                                                            cnode.left.cars,
                                                            cnode.left.left,
                                                            cnode.left.right)
            
                else:
                        if cnode.isLeftChild():
                                cnode.right.parent = cnode.parent
                                cnode.parent.left = cnode.right
                        elif cnode.isRightChild():
                                cnode.right.parent = cnode.parent
                                cnode.parent.right = cnode.right
                        else:
                                cnode.replaceNodeData(cnode.right.make,
                                                            cnode.right.model,
                                                            cnode.right.cars,
                                                            cnode.right.left,
                                                            cnode.right.right)
                                
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
    
assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""