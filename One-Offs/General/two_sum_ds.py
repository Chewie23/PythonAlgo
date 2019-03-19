"""
Design and implement a TwoSum class. It should support 
the following operations: add and find.
add - Add the number to an internal data structure. 
find - Find if there exists any pair of numbers which sum is equal to the value.
"""

class TwoSum():
    def __init__(self):
        self.arr = []

    def add(self, val):
        self.arr.append(val)

    def find(self, target):
        my_list = []
        for n in self.arr:
            if n in my_list:
                return True
            else:
                my_list.append(target - n)
        return False

ts = TwoSum()

for n in range(10):
    ts.add(n)

print(ts.find(4))
print(ts.find(50))
