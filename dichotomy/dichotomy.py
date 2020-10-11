from typing import Callable


def get_mid(a: float, b: float) -> float:
    return (a + b) / 2


def get_root(f: Callable[[float], float], left_endpoint: float, right_endpoint: float, eps: float = 1e-10) -> float:
    endpoint = get_mid(left_endpoint, right_endpoint)
    while right_endpoint - left_endpoint > eps:
        f_left = f(left_endpoint)
        f_endpoint = f(endpoint)
        if f_left > 0 and f_endpoint < 0 or f_left < 0 and f_endpoint > 0:
            right_endpoint = endpoint
        else:
            left_endpoint = endpoint
        endpoint = get_mid(left_endpoint, right_endpoint)

    return endpoint
