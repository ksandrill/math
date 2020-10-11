from dichotomy import get_root
from intervals_finder import *


def main():
    a, b, c, d = 1, -6, 11, -6
    print(str(a) + "x^3 +" + str(b) + "x^2 +" + str(c) + "x + " + str(d))
    f = get_function(a, b, c, d)
    eps = 0.0000001
    delta = 0.1
    interval_list = find_intervals(f, a, b, c, eps, delta)
    for elem in interval_list:
        print("x=", end=' ')
        if len(elem) == 2:
            print(get_root(f, elem[0], elem[1], eps))
        else:
            print(list.__getitem__(elem, 0))


if __name__ == "__main__":
    main()
