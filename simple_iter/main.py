import math
from typing import Callable


def main():
    print("it's simple solver for xh = lsinx on [-pi/2; pi/2]:")
    l, h = map(float, input("enter l and h: ").split(" "))

    eps = float(input("enter epsilon: "))
    if l < h:
        print("wrong l and h, should be l >= h")
        return
    if l > h:

        x_start: float = float(input("please enter start point in (0, pi/2]: "))
        if x_start <= 0 or x_start > math.pi / 2:
            print("wrong x_start")
            return
        root = get_root(x_start, eps, get_function(l, h))
        print(root)
        print(-root)

    print("root: 0")


def get_function(l: float, h: float) -> Callable[[float], float]:
    return lambda x: l * math.sin(x) / h


# def get_diff(l: float, h: float) -> Callable[[float], float]:
#     return lambda x: l * math.cos(x) / h


def get_root(x_start: float, eps: float, func: Callable[[float], float]) -> float:
    x_0: float = x_start
    x: float = func(x_0)
    n: int = 1
    while abs(x - x_0) > eps:
        x_0 = x
        x = func(x_0)
        print("x,i: ", x, n)
        n += 1
    print("iters: ", n)
    return x


if __name__ == '__main__':
    main()
