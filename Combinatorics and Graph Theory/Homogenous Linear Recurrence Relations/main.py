import numpy as np


class LinHomoRecRel:
    def __init__(
        self, h: np.ndarray, order: int, coefficients: np.ndarray = None
    ) -> None:
        if type(coefficients) != np.ndarray:
            coefficients = np.ones(order)
        if h.size != order:
            raise ValueError
        self.h = h
        self.order = order
        self.coefficients = coefficients

    def calc(self, n: int):
        result = np.zeros(n)

        result[0 : self.order] = self.h

        for i in range(self.order, n):
            result[i] = int(np.dot(result[i - self.order : i], self.coefficients.T))

        return result


fib = LinHomoRecRel(np.array([1, 1]), 2)
print(fib.calc(10))


lin = LinHomoRecRel(np.array([1, 2, 3]), 3, np.array([4,8,6]))
print(lin.calc(10))
