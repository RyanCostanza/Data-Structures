class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make and self.model > rhs.model:
            return True
        elif self.make == rhs.make and self.model == rhs.model and self.year > rhs.year:
            return True
        elif self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price > rhs.price:
            return True
        else:
            return False

    def __lt__(self, rhs):
        return rhs.__gt__(self)

    def __eq__(self, rhs):
        if self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price == rhs.price:
            return True
        else:
            return False

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"