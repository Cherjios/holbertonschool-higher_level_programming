#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)-1
    print('{} argument{}{}'
          .format(n, "" if n is 1 else "s", "." if n is 0 else":"))
    for i in range(n):
        print('{}: {}'.format(i + 1, sys.argv[i + 1]))
