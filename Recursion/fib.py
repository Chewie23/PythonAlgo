#Of course, the stereotypical fibonnaci sequence

#The fibonnaci sequence:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#The next number is adding the previous two numbers
#Always starts with 0 and 1

#Personally, I think you can do this iteratively, but we're here for recursion

#Goal: Print out the sequence to the nth number
#n = 7
#0, 1, 1, 2, 3, 5, 8

def iter_fib(n):
    my_fib = [0, 1]
    for x in range(n):
        my_fib.append(my_fib[-2] + my_fib[-1])

    return my_fib

def recur_sigma(n):
    #This sums up the number
    if n == 0:
        return n
    return n + recur_sigma(n-1)

def recur_fib(n):
    #We want "n" to be the counter

    #I peeked at the answer. I still can't unthink out of iteration.
    #But yeah, there are two base cases here, which is the beginning 
    #Fun
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2)




print(iter_fib(7))

print(recur_sigma(5))

print(recur_fib(7))

