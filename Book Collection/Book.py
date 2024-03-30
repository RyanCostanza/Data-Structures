class Book:
    def __init__(self, title="", author="", year=None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

    def __gt__(self, other):
        sa = self.author.lower()
        oa = other.author.lower()
        sy = self.year
        oy = other.year
        st = self.title.lower()
        ot = other.title.lower()
        if sa > oa:
            return True
        elif sa == oa and sy > oy:
            return True
        elif sa == oa and sy == oy and st > ot:
            return True
        else:
            return False

#b = Book("Ready Player One", "Cline, Ernest", 2011)
#print(b.getBookDetails())