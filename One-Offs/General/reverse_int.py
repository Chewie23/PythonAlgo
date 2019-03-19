"""
Reverse an int

Ex.

4432 -> 2344
"""
def rev_int(my_int):
    if my_int < 0:
        neg = True
        my_int *= -1
    else:
        neg = False

    dig_list = []
    while my_int:
        rem = my_int % 10
        my_int = my_int // 10
        dig_list.append(str(rem))

    #Stringfy an integer is...okay. It's servicable to convert int -> str ->
    #int
    result = int("".join(dig_list))
    if neg:
        return result * -1
    return result

my_int = 4321

print(rev_int(my_int))
