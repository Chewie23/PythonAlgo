"""
1 Two SumGiven an array of integers, find two numbers such that 
they add up to a specific targetnumber.The function twoSum 
should return indices of the two numbers such that they 
addup to the target, where index1must be less than index2. 

For example:Input: numbers={2, 7, 11, 15}, target=9Output: index1=0, index2=1
"""

#Plan A:
#Find all the sums. That is VERY time consuming and not very...smart?

#Plan B: 
#

def find_two_sum(arr, target):
    #This is the brute force method
    for n in range(len(arr)):
        for x in range(n, len(arr)):
            if (arr[n] + arr[x] == target) and (n != x):
                return (n, x)
    return "No sum"

def find_two_sum_elegant(arr, target):
    #The more elegant way
    #Uses several things, but mainly checking if the difference of the target
    #is in the given list. Which we track in a dictionary
    #And we have the key == the difference, since we only care if it is ahead
    #of us or not
    my_dict = {}
    result = []
    for n in arr:
        if n in my_dict.keys():
            print(n)
            result = [my_dict[n], n]
        else:
            #Need to have (target - n) since "n" will be before and we want to
            #see if it will be there after
            my_dict[target - n] = n
    return result
    

arr = [2, 22, 11, 15]

target = 33

print(find_two_sum_elegant(arr, target))



