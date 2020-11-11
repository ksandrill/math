import matplotlib.pyplot as plt

from diff_utils import *


def drawer(sub: plt.Subplot, x_list: List[float], y_dots: List[float], y_func: list[float], title: str):
    sub.plot(x_list, y_func)
    sub.plot(x_list, y_dots, 'ro')
    sub.grid(axis='both')
    sub.set_title(title)
    sub.set_xlabel('$x$')
    sub.set_ylabel('$y$')


def main():
    a, b = 0.0, 1.0

    n = int(input("enter n (int): "))
    if n < 2:
        print("n  should be > 2")
        exit(-1)
    h: float = (b - a) / n
    x_list = init_grid(a, h, n)
    y_ac1_list = get_ap1_sol(a, 1, h, n, x_list)
    y_ac2_list = get_ap2_sol(a, 1, h, n, x_list)
    y_ac4_list = get_ap4_sol(a, 1, h, n, x_list)

    fig = plt.figure()
    drawer(fig.add_subplot(2, 1, 1), x_list, y_ac1_list, list(map(get_real_y_value, x_list)), "1th acc")
    drawer(fig.add_subplot(2, 2, 3), x_list, y_ac2_list, list(map(get_real_y_value, x_list)), "2th acc")
    drawer(fig.add_subplot(2, 2, 4), x_list, y_ac4_list, list(map(get_real_y_value, x_list)), "4th acc")
    fig.set_figwidth(12)
    fig.set_figheight(12)

    plt.show()


if __name__ == '__main__':
    main()
