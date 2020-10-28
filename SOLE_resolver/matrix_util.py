from typing import List


def read_matrices(matrix: List[List[float]], vector: List[float], file_path: str) -> bool:
    got_d: bool = False
    with open(file_path, 'r') as file:
        line = file.readline()
        if line != 'A\n':
            return False
        for lines in file.readlines():
            if lines[0] == 'd':
                got_d = True
                continue
            if not got_d:
                matrix.append(list(map(float, lines.strip("\n").split(" "))))
            if got_d:
                vector.append(float(lines[0]))
        if not got_d:
            return False
        return True


def check_dimension(matrix: List[List[float]], vector: [float]) -> int:
    matrix_colls: int = len(matrix)
    if matrix_colls != len(vector):
        return 2
    for i in range(1, matrix_colls):
        if len(matrix[i]) != len(matrix[i - 1]):
            return 1
    return 0


def write_answer(answer: List[float], file_path: str):
    with open(file_path, 'w') as file:
        file.write("x" + "\n")
        for i in range(len(answer)):
            file.write(str(answer[i]) + "\n")

