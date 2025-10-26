"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

# make a class that extends list, has a contains(list) method
class MyList(list):
    def __init__(self, *args):
        super().__init__(*args)
    def contains(self, some_list):
        if some_list == []:
            return True
        starts = range(len(self) - len(some_list) + 1)
        for start in starts:
            if some_list == self[start:start + len(some_list)]:
                return True
        return False
        
    

def sublist(list_one, list_two):
    A = MyList(list_one)
    B = MyList(list_two)
    
    if A == B: return EQUAL
    if B.contains(A): return SUBLIST
    if A.contains(B): return SUPERLIST
    return UNEQUAL