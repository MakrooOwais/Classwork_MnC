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


def f(x: float, y: float):
    return (2 - y**2) / (5 * x)


class ForwardEuler:
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
        Function forward_euler: Implements the forward Euler method for solving a first-order ordinary differential equation (ODE).
        Parameters:
            f (callable): The function representing the first-order ODE dy/dx = f(x, y).
            h (float): The step size for discretizing the interval [a, b].
            a (float): The initial value of x.
            b (float): The final value of x.
            y_a (float): The initial value of y at x = a.
        Returns:
            list[float]: A list containing the approximate values of y for each step of the Euler method.
        """
        x = self.param.get
        h, a, b, y_a, error = x("h"), x("a"), x("b"), x("y_a"), x("error")
        n = int((b - a) / h)
        if n != 1:
            n += 1
        results = [0 for _ in range(n)]

        results[0] = round(y_a + h * f(a, y_a), len(str(error)))

        for i in range(1, n):
            results[i] = round(
                results[i - 1] + h * f(a + (i - 1) * h, results[i - 1]), len(str(error))
            )

        results.insert(0, y_a)
        return results


# Main Program:
# - The main program uses the forward Euler method to approximate the solution of the first-order ODE dy/dx = 2x + y.
# - The `forward_euler` function is called with the provided parameters to obtain the approximate values of y.
# - The `print` function is used to display the list of approximate values of y at different steps of the Euler method.
if __name__ == "__main__":
    forward_euler = ForwardEuler()
    forward_euler.set_param(0, 1, 0.1, 1)
    print(forward_euler.solve(f_1))
