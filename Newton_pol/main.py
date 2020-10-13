from func import get_function
from polynomial import get_diff, get_polynomial


def fixed(number, digits):
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
        nodes_values = list(map(get_function, nodes))
        arr = get_diff(nodes, nodes_values)
        data: (float, float) = get_polynomial(x, arr, nodes)
        print("answer: ", fixed(data[0], 2))
        print("accuracy: ", fixed(data[1], 2))
        with open('answers.txt', 'a') as file:
            file.write("[" + str(a) + "; " + str(b) + "]\n")
            file.write("    \tn: " + str(n))
            file.write("    \th: " + str(n) + "\n")
            file.write("    \tx: " + str(x) + "\n")
            file.write(("   \tanswer: " + str(fixed(data[0], 2)) + "\n"))
            file.write("    \taccuracy: " + fixed(data[1], 2) + "\n")


if __name__ == "__main__":
    main()
