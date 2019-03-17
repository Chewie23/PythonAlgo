"""
Reverse an int

Ex.

4432 -> 2344
"""

def rev_int(my_int):
    #Errors out. Since int != iterable
    for n in my_int:
        print(n)

my_int = 4432

rev_int(my_int)
