from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.left = None
        self.right = None
        self.parent = None
        self.make = car.make
        self.model = car.model
        self.cars = [car]
    
    def getMake(self): 
        return self.make

    def getModel(self): 
        return self.model

    def getParent(self): 
        return self.parent

    def setParent(self, parent): 
        self.parent = parent
    
    def getLeft(self): 
        return self.left

    def setLeft(self, left): 
        self.left = left
    
    def getRight(self): 
        return self.right

    def setRight(self, right): 
        self.right = right
    
    def __str__(self):
        result = ''
        result += '\n'.join(str(car) for car in self.cars)
        result += '\n'
        return result

    def __gt__(self, other):
        if self.make > other.make:
            return True
        elif self.make == other.make and self.model > other.model:
            return True     
        else:
            return False
  
    def __eq__(self, other):
        if other is not None:
            if (self.make == other.make) and (self.model == other.model):
                return True
        else:
            return False

    def __lt__(self, other):
        if self.make < other.make:
            return True
        elif self.make == other.make and self.model < other.model:
            return True     
        else:
            return False

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            elif self.isRightChild():
                self.parent.right = None
            else:
                self = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


    def replaceNodeData(self,make,model,cars,leftchild,rightchild):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = leftchild
        self.right = rightchild
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
        
    def findSuccessor(self):
        successor = None
        if self.hasRightChild():
            successor = self.right.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.findSuccessor()
                    self.parent.right = self
        return successor
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current