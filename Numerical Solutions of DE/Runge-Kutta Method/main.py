def f_1(x: float, y: float) -> float:
    return -2 * x * y**2


def f_2(x: float, y: float) -> float:
    return x**2 + y**2


class RungeKuttaMethod:
    coefficients_dict = {2: [0, 1], 3: [0, 1 / 2, 1], 4: [0, 1 / 2, 1 / 2, 1]}
    coefficients_k_dict = {
        2: [1 / 2, 1 / 2],
        3: [1 / 6, 2 / 3, 1 / 6],
        4: [1 / 6, 1 / 3, 1 / 3, 1 / 6],
    }

    def __init__(self, order: int) -> None:
        self.order: int = order
        self.result: float = 0
        self.k_i = [None] * order

    def solve(self, f: callable, a: float, y_a: float, h: float) -> float:
        coefficients = self.coefficients_dict.get(self.order)
        coefficients_k = self.coefficients_k_dict.get(self.order)

        self.k_i[0] = f(a, y_a)
        for i in range(1, self.order):
            self.k_i[i] = f(
                a + coefficients[i] * h, y_a + coefficients[i] * self.k_i[i - 1] * h
            )

        self.result = y_a

        for i in range(self.order):
            self.result += h * coefficients_k[i] * self.k_i[i]
        return round(self.result, 6)

    def getKs(self) -> list:
        return self.k_i


secondOrderRK = RungeKuttaMethod(2)
thirdOrderRK = RungeKuttaMethod(3)
fourthOrderRK = RungeKuttaMethod(4)

print(secondOrderRK.solve(f_1, 0, 1, 0.2))
print(secondOrderRK.solve(f_2, 1, 1.2, 0.05))

print(thirdOrderRK.solve(f_1, 0, 1, 0.2))
print(thirdOrderRK.solve(f_2, 1, 1.2, 0.05))

print(fourthOrderRK.solve(f_1, 0, 1, 0.2))
print(fourthOrderRK.solve(f_2, 1, 1.2, 0.05))
