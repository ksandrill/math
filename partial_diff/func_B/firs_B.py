from typing import Optional, List

import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


def print_2d_list(my_list: List[List[float]], N: int, T: int):
    for i in range(T):
        for j in range(N):
            print(my_list[i][j], end=" ")
        print()


def maybe_get_g_value(x: float) -> Optional[float]:
    if -1 <= x < 0:
        return 2.0
    if 0 <= x <= 3:
        return 1.0
    return None


def get_f_value():
    return 2


def get_a_value(x: float):
    return x


def init_left_border(u_list: [List[float]], T: int):
    for i in range(1, T):
        u_list[i][0] = get_f_value()


def init_start_values(u_list: [List[float]], x0: float, h: float, N: int) -> int:
    for i in range(0, N):
        # print(x0 + i * h)
        g_value = maybe_get_g_value(x0 + i * h)
        if g_value is not None:
            u_list[0][i] = g_value
        else:
            u_list[0][i] = g_value
    return 0


def evaluate(u_list: List[List[float]], N: int, T: int, a_list: List[float], tay_list: List[float], h: float):
    for n in range(0, T - 1):
        for j in range(1, N):
            r = a_list[n] * tay_list[n] / h
            u_list[n + 1][j] = (1 - r) * u_list[n][j] + r * u_list[n][j - 1]


def get_real_u(N: int, T: int, x0: float, h: float, a_list: List[float], time_list: List[float]) -> List[List[float]]:
    real_u = [[0.0] * N for i in range(T)]
    for n in range(T):
        for j in range(N):
            x = j * h + x0
            print(j, ": ", x, end=" ")
            time = time_list[n]
            a = a_list[n]
            g = maybe_get_g_value(x - a * time)
            print(g)
            if g is not None:
                real_u[n][j] = g
            else:
                real_u[n][j] = get_f_value()
    return real_u


def get_max_a(N: int, x0: float, h: float):
    max_a = 0
    for i in range(N):
        cur_a = get_a_value(x0 + i * h)
        if max_a <= cur_a:
            max_a = cur_a
    return max_a


def fill_params_lists(a_list: List[float], tay_list: List[float], time_list: List[float], N: int, T: int, x0: float,
                      h: float,
                      z: float):
    a_list[0] = get_max_a(N, x0, h)
    zh = z * h
    tay_list[0] = 0
    time_list[0] = 0
    for i in range(1, T):
        a_list[i] = get_max_a(N, x0 - a_list[i - 1] * tay_list[i - 1], h)
        tay_list[i] = zh / a_list[i]
        time_list[i] = time_list[i - 1] + tay_list[i]


def main():
    N, T = map(int, input("enter N and T: ").split(" "))
    x0, x_last = map(float, input("enter x0, x_last: ").split(" "))
    z = float(input("enter z: "))
    h: float = (x_last - x0) / N
    a_list: List[float] = [42] * T
    tay_list: List[float] = [42] * T
    time: List[float] = [42] * T

    fill_params_lists(a_list, tay_list, time, N, T, x0, h, z)

    u_list = [[42] * N for i in range(T)]
    init_left_border(u_list, T)
    err_code = init_start_values(u_list, x0, h, N)
    print("evaluate ")
    if err_code != 0:
        print("can't init start values")
        return -1
    real_u_list = get_real_u(N, T, x0, h, a_list, time)
    evaluate(u_list, N, T, a_list, tay_list, h)

    x_list = [x0 + i * h for i in range(N)]

    fig, ax1 = plt.subplots()
    frames = []
    print_2d_list(real_u_list, N, T)
    for tay in range(0, T):
        line, = ax1.plot(x_list, u_list[tay], 'ro')
        line1, = ax1.plot(x_list, real_u_list[tay], 'b')
        frames.append([line, line1])

    animation = ArtistAnimation(fig, frames, interval=2000, blit=False, repeat=True)
    plt.show()
    animation.save('try.gif', writer='Pillow', fps=2)


if __name__ == "__main__":
    main()
