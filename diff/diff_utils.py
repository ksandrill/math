import math
from typing import List


def get_g_value(x: float) -> float:
    return math.sin(x)


def get_real_y_value(x: float) -> float:
    return 2 - math.cos(x)


# 2 - math.cos(x) for y(0) = 1 and g = sin_x

def get_ap4_sol(x0: float, y0: float, h: float, n: int, x_list: List[float]) -> List[float]:
    g_list: List[float] = [0] * n
    y_list: List[float] = [0] * n
    g_list[0] = get_g_value(x0)
    y_list[0] = y0
    g_list[1] = get_g_value(x_list[1])
    y_list[1] = (g_list[0] + g_list[1] + get_g_value(h)) * h / 3 + y_list[0]
    for i in range(2, n):
        g_list[i] = get_g_value(x_list[i])
    for i in range(1, n - 1):
        y_list[i + 1] = (g_list[i + 1] + g_list[i - 1] + 4 * g_list[i]) * h / 3 + y_list[i - 1]
    return y_list


def get_ap2_sol(x0: float, y0: float, h: float, n: int, x_list: List[float]) -> List[float]:
    g_list: List[float] = [0] * n
    y_list: List[float] = [0] * n
    g_list[0] = get_g_value(x0)
    y_list[0] = y0
    g_list[1] = get_g_value(x_list[1])
    y_list[1] = g_list[0] * h + y_list[0]
    for i in range(2, n):
        g_list[i] = get_g_value(x_list[i])
    for i in range(1, n - 1):
        y_list[i + 1] = (g_list[i + 1] + g_list[i - 1]) * h + y_list[i - 1]
    return y_list


def get_ap1_sol(x0: float, y0: float, h: float, n: int, x_list: List[float]) -> List[float]:  # first accuracy #
    g_list: List[float] = [0] * n
    y_list: List[float] = [0] * n
    g_list[0] = get_g_value(x0)
    y_list[0] = y0
    for i in range(1, n):
        g_list[i] = get_g_value(x_list[i])
        y_list[i] = g_list[i - 1] * h + y_list[i - 1]
    return y_list


def init_grid(x0: float, h: float, n: int) -> List[float]:
    x_list: List[float] = [0] * n
    x_list[0] = x0
    for i in range(1, n):
        x_list[i] = x_list[i - 1] + h
    return x_list
