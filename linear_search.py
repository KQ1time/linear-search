# Linear search for AlgoPy

def linear_search(array, item):
    for i, el in enumerate(array):
        if el == item:
            return i
    return -1
