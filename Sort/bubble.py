#Bubble sort
#The gist of it is to go through an array, two at a time and rearrange as
#needed

disarray = [1, 3, 5, 6, 2, 4]

#TECHNICALLY a while loop would be more efficient, since we can break when
#earlier. But this will ALWAYS have a O(n^2) complexity
def bubble_sort_for(array):
    for n in range(len(disarray)):
        for i in range(len(disarray)):
            x = i + 1
            try:
                if disarray[i] > disarray[x]:
                    disarray[x], disarray[i] = disarray[i], disarray[x]
            except IndexError:
                continue

def bubble_sort_while(array):
    #This is more efficient since we track the swapping and
    #don't have to go through the entire array
    while True:
        swapped = False
        for i in range(len(array)):
            x = i + 1
            try:
                if disarray[i] > disarray[x]:
                    disarray[x], disarray[i] = disarray[i], disarray[x]
                    swapped = True
            except IndexError:
                continue
        if not swapped:
            break



print(disarray)
bubble_sort_while(disarray)
print(disarray)
