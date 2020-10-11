from math import exp
from typing import List


def get_function(x: float) -> float:
    return x ** 3 - exp(x) + 1


def get_diff(nodes_values: List[float]) -> List[List[float]]:
    diff: list = [[]]
    diff[0] = nodes_values.copy()

    return diff


def get_polynom():
    ...


def get_accuracy():
    ...


def main():
    a, b = map(float, input("write [a, b]: ").split(' '))
    n = int(input("write n: "))  # число узлов
    h = (b - a) / n  # шаг сетки
    nodes = []
    for i in range(n):
        nodes.append(a + h * i)
    nodes_values = list(map(get_function, nodes))
    print(get_diff(nodes_values))


if __name__ == "__main__":
    main()
