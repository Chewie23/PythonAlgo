#Going to reverse a string via recursion

def rev_str(string):
    #Crap. I keep peeking at answers. I mean, I know I can internalize after
    #some practice, but this is kind of worrying that recursion isn't coming
    #back after some time
    if string == "":
        return string
    return string[-1] + rev_str(string[:-1])


my_str = "12345"

print(rev_str(my_str))
