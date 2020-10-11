from math import sqrt

from math_func import *


def find_intervals(f: Callable[[float], float], a: float, b: float, c: float, eps: float, delta: float):
    der_a, der_b, der_c = get_der_coef(a, b, c)
    D = der_b ** 2 - 4 * der_a * der_c
    print("D =", D)
    interval_list = []
    if D < 0:
        _negative_disk_worker(f, eps, interval_list)
    elif D > 0:
        sqrt_disk = sqrt(D)
        der_x1 = (-der_b - sqrt_disk) / (2 * der_a)
        der_x2 = (-der_b + sqrt_disk) / (2 * der_a)
        _positive_disk_worker(f, der_x1, der_x2, eps, interval_list)
    else:
        x_ = der_b / (2 * der_a)
        interval_list.append([x_, x_, x_])
    return calculate_root_intervals(f, delta, delta, interval_list)


def _negative_disk_worker(f: Callable[[float], float], eps: float, interval_list: list):
    f_0 = f(0)
    print(f(0))
    if abs(f_0) < eps:
        interval_list.append([0])
    elif f_0 > 0:
        interval_list.append([["-inf", 0]])
    elif f_0 < 0:
        interval_list.append([[0, "+inf"]])


def _positive_disk_worker(f: Callable[[float], float], x1: float, x2: float, eps: float, interval_list: list):
    f_x1, f_x2 = f(x1), f(x2)

    if f_x1 < -eps and f_x2 < -eps:  # 1
        interval_list.append([x2, "inf"])
        # print("#1")
    elif abs(f_x1) < eps and f_x2 < -eps:  # 2
        interval_list.append([x1])
        interval_list.append([x2, "inf"])
        # print("#2")
    elif f_x1 > eps and f_x2 < -eps:  # 3
        interval_list.append(["-inf", x1])
        interval_list.append([x1, x2])
        interval_list.append([x2, "inf"])
        # print("#3")

    elif f_x1 > eps > abs(f_x2):  # 4
        interval_list.append(["-inf", x1])
        interval_list.append([x2])
    # print("#4")

    elif f_x1 > eps and f_x2 > eps:
        interval_list.append(["-inf", x1])
    # print("#5")
    # print(interval_list)


def calculate_root_intervals(f: Callable[[float], float], delta_left: float, delta_right: float, interval_list: list):
    new_interval_list = []

    for elem in interval_list:
        cur_delta_left = 0
        cur_delta_right = delta_right
        if len(elem) > 1:
            if len(elem) == 2:
                if elem[0] == "-inf":
                    cur_delta_left = delta_left
                    elem[0] = elem[1]
                if elem[1] == "inf":
                    elem[1] = elem[0]
            if len(elem) == 3:
                cur_delta_left = delta_left
            left_bord = elem[0] - cur_delta_left
            right_bord = elem[1] + delta_right
            while f(left_bord) * f(right_bord) >= 0:
                left_bord = left_bord - cur_delta_left
                right_bord = right_bord + cur_delta_right
            new_interval_list.append([left_bord, right_bord])
        else:
            new_interval_list.append(elem)

    return new_interval_list
