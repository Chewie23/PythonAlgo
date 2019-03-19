"""
Reverse a string

Try in place, but pretty sure that is impossible in Python

Can do it with a list? So that would be a character array of sorts?
"""

my_arr = ["a", "b", "c", "d", "e", "f"]

#My solution. Does work, but is expensive and relies on Python internal methods
def reverse_arr(my_arr):
    for n in range(len(my_arr)):
        last = my_arr.pop()
        my_arr.insert(n, last)

def reverse_arr_elegant(my_arr):
    #Stolen from here:
    #https://pythonadventures.wordpress.com/2011/06/29/reverse-a-string-or-list-in-place/
    #I like this since this does NOT rely on internal Python methods

    #It uses the beginning and end of the array to "flip" it around something
    #in the middle (thus the range(size // 2) thing
    #The "i" will proceed normally through the list and the "end_pt" will be
    #going from the back and will flip. This is beautiful and elegant. I need
    #more practice
    size = len(my_arr)
    for i in range(0, size // 2):
        end_pt = size - 1 - i
        print("i: {}, end_pt: {}".format(i, end_pt))
        my_arr[i], my_arr[end_pt] = my_arr[end_pt], my_arr[i]

reverse_arr_elegant(my_arr)
print(my_arr)
