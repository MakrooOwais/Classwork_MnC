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


def modFEM(f: callable, h: float, a: float, b: float, y_a: float):
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

    n = int((b - a) / h)

    results = [0.0 for _ in range(n)]
    results[0] = y_a

    for i in range(1, n):
        results[i] = results[i - 1] + h * f(a + (i - 1) * h, results[i - 1])
        temp = results[i - 1] + (h / 2) * (
            f(a + (i - 1) * h, results[i - 1]) + f(a + i * h, results[i])
        )
        while abs(results[i] - temp) > 10e-5:
            results[i] = temp
            temp = results[i - 1] + (h / 2) * (
                f(a + (i - 1) * h, results[i - 1]) + f(a + i * h, results[i])
            )

        results[i] = round(results[i], 5)

    return results


print(modFEM(f_1, 0.2, 0, 1, 1))
