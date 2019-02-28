#Recursion bubble sort. If you though regular bubble sort was bad

#Remember, it's comparing two elements, and swapping. Then keep on going
#through until no more swapping

#Iteratively, we have a swapping bool, and a while loop
#Or we have outer for loop that will go through ALL of the array

def bubble(arr):
    #This just iterates through it
    #What is the smallest bit of work that I can tease out of it
    if len(arr) == 0:
        return
    print(arr[0])
    bubble(arr[1:])

disarray = [1, 4, 6, 5, 3, 2]

bubble(disarray)
