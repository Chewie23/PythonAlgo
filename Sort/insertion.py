#This one is sort of like bubble sort. Sort of
#It organizes based on two halves: sorted and unsorted.
#Will continually resort the sorted portion with an unsorted element
disarray = [1, 3, 4, 6, 5, 2]

def insertion_sort(arr):
    for n in range(len(arr)):
        for i in range(0, n):
            if arr[i] > arr[n]:
                arr[n], arr[i] = arr[i], arr[n]

print(disarray)
insertion_sort(disarray)
print(disarray)

