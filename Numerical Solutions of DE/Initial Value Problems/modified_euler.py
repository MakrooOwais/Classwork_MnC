def f_1(x: float, y: float) -> float:
    """
    Function f_1: Defines a simple mathematical function 2x + y and returns the result.
    Parameters:
        x (float): The input value for variable x.
        y (float): The input value for variable y.
    Returns:
        float: The result of the function 2x + y.
    """
    return 2 * x + y


class ModFEM:
    def __init__(self) -> None:
        self.param = {"h": None, "a": None, "b": None, "y_a": None, "error": 10e-3}

    def set_param(self, a: float, b: float, h: float, y_a: float, error: float = None):
        self.param["h"] = h
        self.param["a"] = a
        self.param["b"] = b
        self.param["y_a"] = y_a
        self.param["error"] = error or self.param.get("error")

    def solve(self, f: callable):
        """
        Function modFEM: Implements the modified forward Euler method for solving a first-order ordinary differential equation (ODE).
        Parameters:
            f (callable): The function representing the first-order ODE dy/dx = f(x, y).
            h (float): The step size for discretizing the interval [a, b].
            a (float): The initial value of x.
            b (float): The final value of x.
            y_a (float): The initial value of y at x = a.
        Returns:
            list[float]: A list containing the approximate values of y for each step of the Modified Euler method.
        """
        x = self.param.get
        h, a, b, y_a, error = x("h"), x("a"), x("b"), x("y_a"), x("error")
        n = int((b - a) / h)
        if n != 1:
            n += 1

        results = [0.0 for _ in range(n)]
        results[0] = y_a

        for i in range(1, n):
            results[i] = results[i - 1] + h * f(a + (i - 1) * h, results[i - 1])
            temp = results[i - 1] + (h / 2) * (
                f(a + (i - 1) * h, results[i - 1]) + f(a + i * h, results[i])
            )
            while abs(results[i] - temp) > error:
                results[i] = temp
                temp = results[i - 1] + (h / 2) * (
                    f(a + (i - 1) * h, results[i - 1]) + f(a + i * h, results[i])
                )

            results[i] = round(results[i], len(str(error)))

        return results


if __name__ == "__main__":
    modfem = ModFEM()
    modfem.set_param(0, 1, 0.1, 1)
    print(modfem.solve(f_1))
