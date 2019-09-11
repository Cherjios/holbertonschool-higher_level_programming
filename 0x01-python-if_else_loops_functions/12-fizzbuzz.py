#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        d3 = n % 3
        d5 = n % 5
        if d3 == 0 and d5 == 0:
            print("FizzBuzz ", end="")
        elif d3 == 0:
            print("Fizz ", end="")
        elif d5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(n), end="")
