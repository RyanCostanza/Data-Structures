from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def getNumberOfBooks(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertBook(self, book):
        new = BookCollectionNode(book)
        if self.head == None:
            self.head = new
        elif book < self.head.getData():
            new.setNext(self.head)
            self.head = new
        else:
            current = self.head
            previous = None
            while current != None and book > current.getData():
                previous = current
                current = current.getNext()
            new.setNext(current)
            previous.setNext(new)

    def getBooksByAuthor(self, author):
        author = author.lower()
        current = self.head
        books = ""
        while current != None:
            if current.getData().getAuthor().lower() == author:
                books += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return books
    
    def getAllBooksInCollection(self):
        current = self.head
        booklist = ""
        while current != None:
            booklist += str(current.getData().getBookDetails()) + "\n"
            current = current.getNext()
        return booklist
    
    def removeAuthor(self, author):
        current = self.head
        previous = None
        while current:
            if current.getData().getAuthor().lower() == author.lower():
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
            else:
                previous = current
            current = current.getNext()
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())