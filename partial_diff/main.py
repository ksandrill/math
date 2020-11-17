import math
from typing import Optional, List

import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


def print_2d_list(my_list: List[List[float]], N: int, T: int):
    for i in range(T):
        for j in range(N):
            print(my_list[i][j], end=" ")
        print()


def maybe_get_g_value(x: float) -> Optional[float]:
    if 0 <= x < 1:
        return 0.0
    if 1 <= x <= 4:
        return math.sin((x - 1) * math.pi / 3)
    if 4 < x <= 5:
        return 0.0
    return


def get_f_value(x: float):
    return 0


def init_left_border(u_list: [List[float]], T: int, x0: float):
    for i in range(1, T):
        u_list[i][0] = get_f_value(x0)


def init_start_values(u_list: [List[float]], x0: float, h: float, N: int) -> int:
    for i in range(0, N):
        # print(x0 + i * h)
        g_value = maybe_get_g_value(x0 + i * h)
        if g_value is not None:
            u_list[0][i] = g_value
        else:
            return -1
    return 0


def evaluate(u_list: List[List[float]], r: float, N: int, T: int):
    for n in range(0, T - 1):
        for j in range(1, N):
            u_list[n + 1][j] = (1 - r) * u_list[n][j] + r * u_list[n][j - 1]


def get_real_u(N: int, T: int, x0: float, y0: float, h: float, t: float, a: float) -> List[List[float]]:
    real_u = [[0.0] * N for i in range(T)]
    for n in range(T):
        for j in range(N):
            x = j * h + x0
            tay = y0 + n * t
            g = maybe_get_g_value(x - a * tay)
            if g is not None:
                real_u[n][j] = g
            else:
                real_u[n][j] = get_f_value(tay - x / a)
    return real_u


def main():
    N, T = map(int, input("enter N and T: ").split(" "))
    x0, x_last = map(float, input("enter x0, x_last: ").split(" "))
    y0, y_last = map(float, input("enter y0, y_last: ").split(" "))
    a = float(input("enter a: "))
    h: float = (x_last - x0) / N
    t: float = (y_last - y0) / T

    u_list = [[42] * N for i in range(T)]
    init_left_border(u_list, T, x0)
    err_code = init_start_values(u_list, x0, h, N)
    # print_2d_list(u_list, N, T)
    print("evaluate ")
    if err_code != 0:
        return -1
    r: float = a * t / h
    print("r: ", r)

    print("r should be < 1")

    print("r = ", r)
    evaluate(u_list, r, N, T)
    real_u = get_real_u(N, T, x0, y0, h, t, a)
    print("real:")
    print_2d_list(real_u, N, T)
    # print("not real:")
    # print_2d_list(u_list, N, T)
    x_list = [x0 + i * h for i in range(N)]
    fig, ax1 = plt.subplots()
    frames = []
    for tay in range(0, T):
        line, = ax1.plot(x_list, u_list[tay], 'ro')
        line1, = ax1.plot(x_list, real_u[tay], 'b')
        frames.append([line, line1])
    animation = ArtistAnimation(fig, frames, interval=2000, blit=False, repeat=True)
    plt.show()
    animation.save('try.gif',
                  writer='Pillow',
                  fps=2)


if __name__ == "__main__":
    main()
