#This is recursion practice, because eff me, quicksort is hard to implement

#Let's iterate through a string, via recursion

def iterate(string):
    #I was doing this all wrong logically. The base case is to catch when it
    #should end. 
    if string:
        print(string[0])
        iterate(string[1:])
    

my_str = "recursion"

iterate(my_str)


"""
Post mortem:

    Recursion is all about the end goal. Or the "base case". When should it
    break out and start returning up the stack

    Then comes the actual "work", which is passed on UNTIL the base case. So
    yeah, base case is super important. 

    I guess the end take away is to ask yourself: when should the recursion
    end?
"""


