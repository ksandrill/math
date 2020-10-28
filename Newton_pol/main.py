from typing import List

from func import get_func_value
from polynomial import get_diff, get_polynomial


def fixed_precision(number: float, digits: int) -> str:
    return f"{number:.{digits}f}"


def main():
    a, b = map(float, input("write [a, b]: ").split(' '))
    n = int(input("write n: "))  # число узлов
    h = (b - a) / n  # шаг сетки
    x = float(input("x: "))  # точка в которой считается полином
    nodes = []
    for i in range(n):
        nodes.append(a + h * i)
    if nodes.count(x) != 0:
        print("it's node")
    else:
        nodes_values = list(map(get_func_value, nodes))
        diffs: List[list[float]] = get_diff(nodes, nodes_values)
        answer, accuracy = get_polynomial(x, diffs, nodes)
        print("answer: ", fixed_precision(answer, 2))
        print("accuracy: ", fixed_precision(accuracy, 2))
        with open('examples/answers.txt', 'a') as file:
            file.write("[" + str(a) + "; " + str(b) + "]\n")
            file.write("    \tn: " + str(n))
            file.write("    \th: " + str(n) + "\n")
            file.write("    \tx: " + str(x) + "\n")
            file.write(("   \tanswer: " + "\t" + str(fixed_precision(answer, 2)) + "\n"))
            file.write("    \taccuracy: " + "\t" + fixed_precision(accuracy, 2) + "\n")


if __name__ == "__main__":
    main()
