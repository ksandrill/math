import math
from typing import List


def fixed_precision(number: float, digits: int) -> str:
    return f"{number:.{digits}f}"


def get_func_value(x: float) -> float:
    return math.exp(x) + 1


def get_integral(a: float, b: float, n: int) -> List[float]:
    h: float = (b - a) / n
    x_l: float = a
    x_r: float = x_l + h
    result: List[float] = [0, 0, 0, 0, 0, 0]

    for i in range(n):
        f_l = get_func_value(x_l)
        f_r = get_func_value(x_r)
        f_m = get_func_value((x_r + x_l) / 2)
        result[0] += h * f_l  # left square
        result[1] += h * f_r  # right square
        result[2] += h * f_m  # mid square
        result[3] += (f_l + f_r) * h / 2  # trapeze
        result[4] += (f_l + f_r + 4 * f_m) * h / 6  # parabola
        result[5] += (f_l + f_r + 3 * get_func_value((2 * x_l + x_r) / 3) + 3 * get_func_value(
            (x_l + 2 * x_r) / 3)) * h / 8  # 3/8
        x_l = x_r
        x_r = x_l + h

    return result


def main():
    a, b = map(float, input("enter ends of intervals (float): ").split(" "))
    n = int(input("enter n (int): "))
    res = get_integral(a, b, n)
    print("left square res : " + fixed_precision(res[0], 3))
    print("right square res : " + fixed_precision(res[1], 3))
    print("mid square res : " + fixed_precision(res[2], 3))
    print("trapeze res : " + fixed_precision(res[3], 3))
    print("parabola res : " + fixed_precision(res[4], 3))
    print("3/8 res : " + fixed_precision(res[5], 3))


if __name__ == '__main__':
    main()
