#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = 0
    for n, arg in enumerate(argv[1:]):
        s += int(arg)
    print('{}'.format(s))
