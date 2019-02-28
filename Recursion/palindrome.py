#Finding out if number is a palindrome.

#I can cheat and just reverse it and compare with original

def rev(string):
    if len(string) == 1:
        return string
    return string[-1] + rev(string[:-1])

def is_palindrome(num):
    my_str = str(num)
    rev_str = rev(my_str)
    if rev_str != my_str:
        return False
    return True 

p_num = 2002
np_num = 2100

#True
print(is_palindrome(p_num)) 

#False
print(is_palindrome(np_num))

