from math import exp
from typing import List


def get_function(x: float) -> float:
    return x ** 3 - exp(x) + 1


def get_diff(nodes: List[float], nodes_values: List[float]) -> List[List[float]]:
    diff: list = [[]]
    diff[0] = nodes_values.copy()
    col = len(diff[0])
    for i in range(1, col):
        aux: list = []
        row = col - i
        for j in range(0, row):
            aux.append((diff[i - 1][j + 1] - diff[i - 1][j]) / (nodes[i + j] - nodes[j]))
        diff.append(aux)

    return diff


def get_polynom(x: float, coef: List[List[float]], nodes: List[float]) -> float:
    w_list: List[float] = []  # w_list[n] = (x -x0)*...(x -xn)
    answer: float = coef[0][0]
    w_list.append(1)
    n = len(coef[0])
    for i in range(1, n):
        w_list.append(w_list[i - 1] * (x - nodes[i - 1]))
        answer = answer + w_list[i] * coef[i][0]
    return answer


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
    arr = get_diff(nodes, nodes_values)
    print(get_polynom(0, arr, nodes))


if __name__ == "__main__":
    main()
