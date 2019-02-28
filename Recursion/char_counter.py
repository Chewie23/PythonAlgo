import collections as c

def count_char(string, d):
    #The basic recursive "for loop" structure
    if string:
        d[string[0]] += 1
        count_char(string[1:], d)



d = c.defaultdict(int)
my_str = "abcdee"

count_char(my_str, d)
print(d)
