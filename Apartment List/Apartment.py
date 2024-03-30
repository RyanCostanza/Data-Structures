class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return f'(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}'
    
    def __gt__(self, other):
        #self worse than other
        conditions = {'bad': 3, 'average': 2, 'excellent': 1}
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent and self.metersFromUCSB > other.metersFromUCSB:
            return True
        elif self.rent == other.rent and self.metersFromUCSB == other.metersFromUCSB and conditions[self.condition] > conditions[other.condition]:
            return True
        else:
            return False
        
    def __lt__(self, other):
        #self better than other
        conditions = {'bad': 3, 'average': 2, 'excellent': 1}
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent and self.metersFromUCSB < other.metersFromUCSB:
            return True
        elif self.rent == other.rent and self.metersFromUCSB == other.metersFromUCSB and conditions[self.condition] < conditions[other.condition]:
            return True
        else:
            return False
    def __eq__(self, other):
        return (self.rent == other.rent and self.metersFromUCSB == other.metersFromUCSB and self.condition == other.condition)