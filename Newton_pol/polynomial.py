from typing import List

from func import get_func_value


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


def get_polynomial(x: float, diffs: List[List[float]], nodes: List[float]) -> (float, float):
    w_list: List[float] = []  # (x -x0)*...(x -x(n-1))
    answer: float = diffs[0][0]
    w_list.append(1)
    n = len(diffs[0])
    for i in range(1, n):
        w_list.append(w_list[i - 1] * (x - nodes[i - 1]))
        answer = answer + w_list[i] * diffs[i][0]
    accuracy = get_accuracy(x, diffs, nodes, w_list[n - 1])
    return answer, accuracy


def get_accuracy(x: float, diffs: List[List[float]], nodes: List[float], w_n: float) -> float:
    acc_diffs: List[List[float]] = list(diffs)
    add_node(x, acc_diffs, nodes)
    nodes.pop()

    accuracy = acc_diffs[len(acc_diffs) - 1][0] * w_n
    return accuracy


def add_node(x: float, diffs: List[List[float]], nodes: List[float]):
    diffs[0].append(get_func_value(x))
    rows = len(diffs)
    for i in range(1, rows):
        j = len(diffs[i - 1]) - 1
        diffs[i].append((diffs[i - 1][j] - diffs[i - 1][j - 1]) / (x - nodes[j - 1]))
    diffs.append([(diffs[rows - 1][1] - diffs[rows - 1][0]) / (x - nodes[0])])
