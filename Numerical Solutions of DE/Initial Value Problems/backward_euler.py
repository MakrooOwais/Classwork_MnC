import sympy as sp

y = sp.symbols("y")


def f_1(x: float, y: float):
    return 2 * x + y


class BackwardEuler:
    def __init__(self) -> None:
        self.param = {"h": None, "a": None, "b": None, "y_a": None, "error": 10e-3}

    def set_param(self, a: float, b: float, h: float, y_a: float, error: float = None):
        self.param["h"] = h
        self.param["a"] = a
        self.param["b"] = b
        self.param["y_a"] = y_a
        self.param["error"] = error or self.param.get("error")

    def solve(self, f: callable):
        x = self.param.get
        h, a, b, y_a, error = x("h"), x("a"), x("b"), x("y_a"), x("error")

        n = int((b - a) / h)
        if n != 1:
            n += 1

        results = [0 for _ in range(n)]

        s = sp.nsolve(y - y_a - h * f(a + h, y), y, y_a)
        results[0] = round(s, len(str(error)))

        for i in range(1, n):
            s = sp.nsolve(y - results[i - 1] - h * f(a + i * h, y), y, results[i - 1])
            results[i] = round(s, len(str(error)))

        results.insert(0, y_a)
        return results


if __name__ == "__main__":
    backward_euler = BackwardEuler()
    backward_euler.set_param(0, 1, 0.1, 1)
    print(backward_euler.solve(f_1))
