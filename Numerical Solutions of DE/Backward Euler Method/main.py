import sympy as sp

y = sp.symbols("y")


def f_1(x: float, y: float):
    return 2 * x + y


def backward_euler(f: callable, a: float, b: float, h: float, y_a: float):
    n = int((b - a) / h)

    results = [0 for _ in range(n)]

    results[0] = y_a

    for i in range(1, n):
        s = sp.nsolve(y - results[i - 1] - h * f(a + i * h, y), y, results[i - 1])
        results[i] = s

    return results


print(backward_euler(f_1, 0, 1, 0.2, 1))
