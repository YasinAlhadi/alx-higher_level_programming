#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    n = 0
    d = sum([x[1] for x in my_list])
    for i in my_list:
        n += i[0] * i[1]
    return (n / d)
