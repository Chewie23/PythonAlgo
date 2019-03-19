#Stolen from here:
#https://stackoverflow.com/questions/24565966/convert-string-to-int-without-int

#This is way more "byte" and "bits" then I would ever want to delve into
#But is nice to know
def atoi(s):
    rtr=0
    for c in s:
        print("ord(c): {}".format(ord(c)))
        print("rtr*10 = {}".format(rtr*10))
        rtr=rtr*10 + ord(c) - ord('0')

    return rtr

print("ord(0): {}".format(ord('0')))

my_str = "123"

print(atoi(my_str))
