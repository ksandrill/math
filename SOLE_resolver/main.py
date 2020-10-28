from typing import List

import matrix_util
import thomas_algo


def fixed_precision(number: float, digits: int) -> str:
    return f"{number:.{digits}f}"


def main():
    matrix: List[List[float]] = []
    vector: List[float] = []
    read: bool = matrix_util.read_matrices(matrix, vector, 'examples/in1.txt')
    if not read:
        print("can't read input")
        print("should be " + "A\n" + "matrix\n" + "d\n" + "vector ")
        exit(-1)
    check_dim: int = matrix_util.check_dimension(matrix, vector)
    if check_dim == 1:
        print("incorrect matrix row size")
        exit(-1)
    if check_dim == 2:
        print("incorrect dimension of vector and matrix")
        exit(-1)
    answer: List[float] = thomas_algo.get_x_vector(matrix, vector)
    for i in range(len(answer)):
        print("x[" + str(i) + "] = ", fixed_precision(answer[i], 3))
    matrix_util.write_answer(answer, 'examples/out1.txt')


if __name__ == "__main__":
    main()
