def f_1(x: float, y: float) -> float:
    return -2 * x * y**2


def f_2(x: float, y: float) -> float:
    return x**2 + y**2


def rungeKuttaMethod(f: callable, a: float, y_a: float, h: float, order: int) -> float:
    coefficients_dict = {2: [0, 1], 4: [0, 1 / 2, 1 / 2, 1]}

    coefficients_k_dict = {2: [1 / 2, 1 / 2], 4: [1 / 6, 1 / 3, 1 / 3, 1 / 6]}

    coefficients = coefficients_dict.get(order)
    coefficients_k = coefficients_k_dict.get(order)

    k_i = [None] * 4

    k_i[0] = f(a, y_a)
    for i in range(1, order):
        k_i[i] = f(a + coefficients[i] * h, y_a + coefficients[i] * k_i[i - 1] * h)

    result = y_a

    for i in range(order):
        result += h * coefficients_k[i] * k_i[i]
    return result


print(rungeKuttaMethod(f_1, 0, 1, 0.2, 4))
print(rungeKuttaMethod(f_2, 1, 1.2, 0.05, 4))

print(rungeKuttaMethod(f_1, 0, 1, 0.2, 2))
print(rungeKuttaMethod(f_2, 1, 1.2, 0.05, 2))
