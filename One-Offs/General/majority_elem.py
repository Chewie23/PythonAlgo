"""
Prompt:
Given a sorted integer array, return the majority element if it exists or -1 otherwise.

"""

import collections as c

my_array = [1, 2, 3, 4, 5, 5, 6, 6]

my_count = c.defaultdict(int)

for n in my_array:
    my_count[n] += 1

#This is a nice way to do it. I was thinking of using lambda with max(), but
#max() cannot return more than one value. So the logic here is to use max()
#As a filter

max_val = max(my_count.values())
res_list = [key for key in my_count.keys() if my_count[key] == max_val]

if res_list == 1:
    print(res_list[0])
else:
    print(-1)
