#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        i = 0
        a = int(sys.argv[i+1])
        op = sys.argv[i + 2]
        b = int(sys.argv[i + 3])
        if op is "+":
            c = add(a, b)
        elif op is "-":
            c = sub(a, b)
        elif op is "*":
            c = mul(a, b)
        elif op is "/":
            c = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, op, b, c))
        exit(0)
