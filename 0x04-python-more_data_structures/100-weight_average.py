#!/usr/bin/python3
def weight_average(my_list=[]):
    suma1 = 0
    suma2 = 0
    for i in my_list:
        suma1 += sum([i[0] * i[1]])
        suma2 += sum([i[1]])
    return (suma1 / suma2)
