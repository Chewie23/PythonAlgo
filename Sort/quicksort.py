#This one is gonna be doozy
#Recursion, my old friend
#The gist here is to choose a pivot point and organize the array around said
#pivot
#THEN repeat. Via recursion

#https://en.wikipedia.org/wiki/Quicksort


#The plan: The pivot will always be the "half" point. That way we can recurse
#easily, rather than choosing a strange arbitrary pivot point

#Let's do this nice and easy like. First up, the actual work/other case of
#swapping elements around
#Then it's the base case, where we exit the function calling each other

def prac_rec(arr):
    #This is a very good way to get the END of an array
    #Not what we need right now
    if len(arr) == 1:
        return arr
    return prac_rec(arr[1:])

def rec_iter(arr):
    #Recursively iterates through stuff
    if arr:
        print(arr[0])
        return rec_iter(arr[1:])

def divide(arr):
    #I want to divide the array into 2 halves, until only 1 element remains
    #Just to print each half as it comes
    
    #This is vaguely close. But god damn is recursion hard to grasp
    if len(arr) == 1:
        return
    print(arr)
    print("pivot: {}".format(len(arr)//2))
    divide(arr[len(arr)//2 :])


disarray = [1, 4, 3, 2, 6, 5]
prac_arr = [4, 1]
pivot = len(disarray) // 2

divide(disarray)
