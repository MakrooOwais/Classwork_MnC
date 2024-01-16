import numpy as np
from matplotlib import pyplot as plt
from math import factorial


class NewtonDivDiff:
    """The NewtonDivDiff class represents the polynomial that interpolates the given points.
    If new points are discovered it can calculate the new coefficients without losing the old calculations thus saving on computation time.
    """

    def __init__(
        self, x: np.ndarray | list[float], f_x: np.ndarray | list[float]
    ) -> None:
        """Initialize the NewtonDivDiff Method for x, f_x.

        Args:
            x (np.ndarray | list[float]): The x coordinate of the points that you want to interpolate over.
            f_x (np.ndarray | list[float]): The f value of the corresponding x values.
        """

        if type(x) is not np.ndarray:
            x = np.array(x)
        self.x = x
        if type(f_x) is not np.ndarray:
            f_x = np.array(f_x)
        self.f_x = f_x
        self.n = len(x)

        self.div_diff = np.zeros((self.n, self.n))
        self.gen_coeff()

    def gen_coeff(self) -> None:
        """This function generates the coefficients of the polynomial using the points given during the initialization."""
        self.div_diff[:, 0] += self.f_x.T

        for j in range(1, self.n):
            for i in range(j, self.n):
                self.div_diff[i][j] = (
                    self.div_diff[i][j - 1] - self.div_diff[i - 1][j - 1]
                ) / (self.x[i] - self.x[i - 1])

        self.coeff = np.array([self.div_diff[i][i] for i in range(self.n)])

    def get_coeff(self) -> np.ndarray:
        """This function returns the coefficients of the interpolating polynomial

        Returns:
            np.ndarray: The coeffient are ordered from the coefficient of lowest exponent of x to the highest exponent of x.
        """
        return self.coeff

    def poly_val(self, target_x: float) -> float:
        """This function returns the extimated value of the function at target_x

        Args:
            target_x (float): The value of x for which you estimate the function.

        Returns:
            float: The extimated value of the function at target_x
        """
        est_value = self.coeff[0]
        product = 1
        for i in range(1, self.n):
            product *= target_x - self.x[i - 1]
            term = self.coeff[i] * product / factorial(i)
            est_value += term

        return est_value

    def poly_mul_points(self, X: np.ndarray | list[float]) -> np.ndarray:
        """This function calculates the estimated value of the function at a range of given values of X.

        Args:
            X (np.ndarray | list[float]): All the values of X at which we want the extimate of f.

        Returns:
            np.ndarray: The estimated value of f at the points in X in the same order.
        """
        if type(X) is not np.ndarray:
            X = np.array(X)
        res = np.zeros(X.shape) + self.coeff[0]
        product = np.ones(X.shape)

        for i in range(1, self.n):
            product *= X - self.x[i - 1]
            term = self.coeff[i] * product / factorial(i)
            res += term

        return res

    def refine_poly(
        self, x_new: np.ndarray | list[float], f_x_new: np.ndarray | list[float]
    ) -> None:
        """This function refines the coefficients of the interpolating polynomial by considering new points on the domain of the original function whose value is already known.

        Args:
            x_new (np.ndarray | list[float]): The x coordinte of new points that we want to use to refine the coefficients
            f_x_new (np.ndarray | list[float]): The value of f for the corresponding x in x_new
        """
        if type(x_new) is not np.ndarray:
            x_new = np.array(x_new)
        if type(f_x_new) is not np.ndarray:
            f_x_new = np.array(f_x_new)
        n_new = self.n + len(x_new)

        self.div_diff = np.append(self.div_diff, np.zeros((len(x_new), self.n)), 0)
        self.div_diff = np.append(
            self.div_diff, np.zeros((self.n + len(x_new), len(x_new))), 1
        )

        self.x = np.append(self.x, x_new, 0)
        self.f_x = np.append(self.f_x, f_x_new, 0)

        self.div_diff[self.n : n_new, 0] += f_x_new

        for j in range(1, n_new):
            for i in range(self.n, n_new):
                self.div_diff[i][j] = (
                    self.div_diff[i][j - 1] - self.div_diff[i - 1][j - 1]
                ) / (self.x[i] - self.x[i - 1])

        self.n = n_new
        self.coeff = np.array([self.div_diff[i][i] for i in range(self.n)])

    def plot(
        self,
        target_x: np.ndarray | list[float] | float | None = None,
        res: int = 10_000,
    ) -> None:
        """This function plots the interpolating polynomial while representing the points of interpolation using blue dots and the target_x with red dots.

        Args:
            target_x (np.ndarray | list[float] | float | None, optional): The values of x for which you want to have the estimated value on the plot. Defaults to None.
            res (int, optional): The no of points in the given domain that you want matplotlib to use for plotting the polynomial. Defaults to 10_000.
        """
        X = np.linspace(self.x[0], self.x[-1], res)
        plt.plot(X, self.poly_mul_points(X))
        plt.scatter(self.x, self.f_x)
        if target_x is not None:
            if type(target_x) is float:
                plt.scatter(target_x, self.poly_val(target_x), c="red")
            else:
                plt.scatter(target_x, self.poly_mul_points(target_x), c="red")
        plt.show()


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5, 6])
    f_x = np.array([14.5, 19.5, 30.5, 53.5, 94.5, 159.5])

    target_x = 4.5
    poly = NewtonDivDiff(x, f_x)
    coeff = poly.get_coeff()

    print(coeff)

    est_value = poly.poly_val(target_x)
    print("Exact Value of f(4.5) =", 71.375)
    print("Estimated Value of f(4.5) =", est_value)
    print("Error in estimation =", np.abs(est_value - 71.375))

    poly.plot(4.5)

    x_new = [7, 8]
    f_x_new = [180.5, 219.5]

    poly.refine_poly(x_new, f_x_new)
    est_value = poly.poly_val(target_x)
    print("Exact Value of f(4.5) =", 71.375)
    print("Estimated Value of f(4.5) =", est_value)
    print("Error in estimation =", np.abs(est_value - 71.375))

    poly.plot()
    poly.plot(4.5)
    poly.plot([1.7, 2.3, 3.3])
