#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print('0 argument.')
    else:
        print('{:d} arguments:'.format(len(argv) - 1))
    for n, s in enumerate(argv):
        if n != 0:
            print('{:d}: {:s}'.format(n, s))
