from typing import List


def get_x_vector(matrix: [List[List[float]]], vector: List[float]):
    alpha_list, betta_list, gamma_list = _forward_stroke(matrix, vector)
    x_vector = _backward_stroke(alpha_list, betta_list, len(matrix))
    return x_vector


def _forward_stroke(matrix: [List[List[float]]], vector: List[float]) -> (List[float], List[float], List[float]):
    gamma_list: List[float] = [matrix[0][0]]
    if matrix[0][0] == 0:
        print("wrong matrix cuz gamma 0 is null")
        exit(-2)
    alpha_list: List[float] = [-matrix[0][1] / gamma_list[0]]
    betta_list: List[float] = [vector[0] / gamma_list[0]]
    n = len(matrix)
    for i in range(1, n - 1):
        gamma_i: float = matrix[i][i] + matrix[i][i - 1] * alpha_list[i - 1]
        if gamma_i == 0:
            print("wrong matrix cuz gamma", i, " is null")
            exit(-2)
        betta_i: float = (vector[i] - matrix[i][i - 1] * betta_list[i - 1]) / gamma_i
        alpha_i: float = -matrix[i][i + 1] / gamma_i
        gamma_list.append(gamma_i)
        alpha_list.append(alpha_i)
        betta_list.append(betta_i)
    last_gamma: float = matrix[n - 1][n - 1] + matrix[n - 1][n - 2] * alpha_list[n - 2]
    last_betta: float = (vector[n - 1] - matrix[n - 1][n - 2] * betta_list[n - 2]) / last_gamma
    gamma_list.append(last_gamma)
    betta_list.append(last_betta)
    return alpha_list, betta_list, gamma_list


def _backward_stroke(alpha_list: List[float], betta_list: List[float], n: int) -> List[float]:
    answer: List[float] = [0] * n
    answer[n - 1] = betta_list[n - 1]
    for i in range(n - 2, -1, -1):
        answer[i] = alpha_list[i] * answer[i + 1] + betta_list[i]
    return answer
