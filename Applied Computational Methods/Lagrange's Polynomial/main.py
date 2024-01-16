import numpy as np
from matplotlib import pyplot as plt


def get_term(
    target_x: np.ndarray | float, idx: int, x: np.ndarray, f_x_i: np.ndarray
) -> np.ndarray | float:
    """This function returns the value of the idx-th in the interpolating polynomial for x = x_target

    Args:
        target_x (float | np.ndarray): The value or values of x for which we want to estimate the valus of f.
        idx (int): The term that we want to evaluate.
        x (np.ndarray): The values of x for which we know the values of f.
        f_x_i (np.ndarray): The values of f for the corresponding x.

    Returns:
        np.ndarray | float: The value of the idx-th term in the Lagrange's polynomial interpolating over the given points.
    """
    term = 1

    for i in range(len(x)):
        if i == idx:
            continue

        term *= (target_x - x[i]) / (x[idx] - x[i])

    return term * f_x_i


def get_poly_val(target_x: float, x: np.ndarray, f_x: np.ndarray) -> float:
    """This function calculates the value of Lagrange's polynomial at the given x.

    Args:
        target_x (float): The point at which we want to estimate f.
        x (np.ndarray): The values of x for which we know the values of f.
        f_x (np.ndarray): The values of f for the corresponding x.

    Returns:
        float: The value of f at target_x estimated using the Lagrange's polynomial.
    """
    est_value = 0

    for i in range(len(x)):
        est_value += get_term(target_x, i, x, f_x[i])

    return est_value


def get_poly_multiple(
    X: np.ndarray | list[float], x: np.ndarray, f_x: np.ndarray
) -> np.ndarray:
    """This function calculates the value of Lagrange's polynomial at all the points in X.

    Args:
        X (np.ndarray | list[float]): The values of x at which we want to estimate the value of f.
        x (np.ndarray): The values of x for which we know the values of f.
        f_x (np.ndarray): The values of f for the corresponding x.

    Returns:
        np.ndarray: The values of f at x, in the same order, estimated using the Lagrange's polynomial.
    """
    if type(X) is not np.ndarray:
        X = np.array(X)

    res = np.zeros(X.shape)

    for i in range(len(x)):
        res += get_term(X, i, x, f_x[i])

    return res


if __name__ == "__main__":
    x = np.array([0, 2, 4, 6])
    f_x = np.array([1, -1, 3, 4])

    x_target = 4.5
    est_value = get_poly_val(x_target, x, f_x)

    print("Exact Value of f(4.5) =", 3.8828125)
    print("Estimated Value of f(4.5) =", est_value)
    print("Error in estimation =", np.abs(est_value - 3.8828125))

    X = np.linspace(np.min(x), np.max(x), 10_000)
    plt.scatter(x, f_x)
    plt.plot(X, get_poly_multiple(X, x, f_x))
    plt.scatter(x_target, est_value, c="red")
    plt.show()
