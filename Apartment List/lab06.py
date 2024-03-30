from Apartment import Apartment

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i+1]:
            return False
    return True

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left_half = apartmentList[:mid]
        right_half = apartmentList[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                apartmentList[k] = left_half[i]
                i += 1
            else:
                apartmentList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            apartmentList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            apartmentList[k] = right_half[j]
            j += 1
            k += 1

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    best_apartment = apartmentList[0]
    return best_apartment.getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    worst_apartment = apartmentList[-1]
    return worst_apartment.getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    a_apartments = []
    for i in apartmentList:
        if i.getRent() <= budget:
            a_apartments.append(i.getApartmentDetails())
    return '\n'.join(a_apartments)
