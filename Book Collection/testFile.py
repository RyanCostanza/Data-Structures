from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def testBook():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    assert b1.getBookDetails() == 'Title: The Shining, Author: King, Stephen, Year: 1977'
    assert b2.getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'

def testBookCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    assert bc.isEmpty() == True
    assert bc.getNumberOfBooks() == 0
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 4
    assert bc.getBooksByAuthor("cline, ernest") == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011' + '\n'
    assert bc.getBooksByAuthor("king, STEPHEN") == 'Title: Rage, Author: King, Stephen, Year: 1977' + '\n' + 'Title: The Shining, Author: King, Stephen, Year: 1977' + '\n' + 'Title: Cujo, Author: King, Stephen, Year: 1981' + '\n'
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011' + '\n' + 'Title: Rage, Author: King, Stephen, Year: 1977' + '\n' + 'Title: The Shining, Author: King, Stephen, Year: 1977' + '\n' + 'Title: Cujo, Author: King, Stephen, Year: 1981' + '\n'
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False
    bc.removeAuthor("King, Stephen")
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011' + '\n'

def testBookCollectionNode():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.head.getData().getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'
    h = bc.head.getNext()
    print(h.getAuthor())

testBook()
testBookCollection()
testBookCollectionNode()