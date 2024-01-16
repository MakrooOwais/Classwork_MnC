def f_1(x: float, y: float) -> float:
    return -2 * x * y**2


def f_2(x: float, y: float) -> float:
    return x**2 + y**2


def f_3(x: float, y: float) -> float:
    return x**2 + 2 * x * y


def f_4(x: float, y: float) -> float:
    return x * y


def f_5(x: float, y: float) -> float:
    return (y**2 - x**2) / (y**2 + x**2)


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
        self.param = {"h": None, "a": None, "b": None, "y_a": None, "error": 10e-3}


    def set_param(self, a: float, b: float, h: float, y_a: float, error: float = None):
        self.param["h"] = h
        self.param["a"] = a
        self.param["b"] = b
        self.param["y_a"] = y_a
        self.param["error"] = error or self.param.get("error")

    def solve_point(self, f: callable, h, a, y_a, error) -> float:
        coefficients = self.coefficients_dict.get(self.order)
        coefficients_k = self.coefficients_k_dict.get(self.order)

        self.k_i[0] = f(a, y_a) * h
        for i in range(1, self.order):
            self.k_i[i] = h * f(
                a + coefficients[i] * h, y_a + coefficients[i] * self.k_i[i - 1]
            )

        self.result = y_a

        for i in range(self.order):
            self.result += coefficients_k[i] * self.k_i[i]
        return round(self.result, len(str(error)))

    def solve(self, f: callable) -> list[float]:
        x = self.param.get
        h, a, b, y_a, error = x("h"), x("a"), x("b"), x("y_a"), x("error")
        n = int((b - a) / h)
        if n != 1:
            n += 1
        results = [None] * n
        results[0] = round(self.solve_point(f, h, a, y_a, error), len(str(error)))

        for i in range(1, n):
            results[i] = round(self.solve_point(f, h, a + i * h, results[i - 1], error), len(str(error)))

        results.insert(0, y_a)

        return results

    def getKs(self) -> list:
        return self.k_i


# secondOrderRK = RungeKuttaMethod(2)
# # thirdOrderRK = RungeKuttaMethod(3)
# fourthOrderRK = RungeKuttaMethod(4)

# # print(secondOrderRK.solve(f_1, 0, 1, 0.2))
# # print(secondOrderRK.solve(f_2, 1, 1.2, 0.05))
# # print(secondOrderRK.solve(f_4, 1.2, 1.244, 0.2))
# # print(secondOrderRK.getKs())

# # print(thirdOrderRK.solve(f_1, 0, 1, 0.2))
# # print(thirdOrderRK.solve(f_2, 1, 1.2, 0.05))

# # print(fourthOrderRK.solve(f_5, 0, 1, 0.5))
# # print(fourthOrderRK.getKs())

# # y = 1

# # for i in range(0, 4):
# #     x = 0 + i * 0.5
# #     y = fourthOrderRK.solve(f_5, x, y, 0.5)
# #     print(y)
# fourthOrderRK.set_param(0, 0.4, 0.1, 1)


# # print(fourthOrderRK.solve(f_2, 1, 1.2, 0.05))
