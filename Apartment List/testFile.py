from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments

def test():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    a6 = Apartment(900, 190, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert (a1 > a2) == True
    assert (a3 > a2) == False
    assert (a6 == a4) == True
    assert (a5 == a4) == False
    assert (a1 < a2) == False
    assert (a3 < a2) == True
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getBestApartment(apartmentList) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad'
    assert getWorstApartment(apartmentList) == '(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad'
    assert getAffordableApartments(apartmentList, 925) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent'

test()