#And the factorial implementation rears it's head

def fact(num):
    #Easy
    if num == 1:
        return num
    return num * fact(num - 1)

num = 5
print(fact(num))
