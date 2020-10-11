from typing import Callable


def get_function(a: float, b: float, c: float, d: float) -> Callable[[float], float]:
    return lambda x: a * x ** 3 + b * x ** 2 + c * x + d


def get_derivative(a: float, b: float, c: float) -> Callable[[float], float]:
    return lambda x: 3 * a * x ** 2 + 2 * b * x + c


def get_der_coef(a: float, b: float, c: float):
    return 3 * a, b * 2, c
