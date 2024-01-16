import numpy as np

from sympy import var, simplify
from sympy.utilities.lambdify import lambdify


def getInput():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    print(
        """If the boundary conditions were to be represented in the form:
          a_0 * y(a) - a_1 * y1(a) = y_a
          b_0 * y(b) + b_1 * y1(b) = y_b"""
    )

    a_0 = float(input("Enter a_0: "))
    a_1 = -float(input("Enter a_1: "))
    y_a = float(input("Enter y_a: "))

    b_0 = float(input("Enter b_0: "))
    b_1 = float(input("Enter b_1: "))
    y_b = float(input("Enter y_b: "))

    return a, b, h, [a_0, a_1, y_a], [b_0, b_1, y_b]


def rk4(f: callable, y_a: list or np.ndarray, a: float, b: float, h: float):
    n = int((b - a) / h)

    ys = [np.array(y_a)]

    for i in range(int(n)):
        k1 = h * np.array(f(a + i * h, *ys[-1]))
        k2 = h * np.array(f(a + i * h + h / 2, *(ys[-1] + k1 / 2)))
        k3 = h * np.array(f(a + i * h + h / 2, *(ys[-1] + k2 / 2)))
        k4 = h * np.array(f(a + (i + 1) * h, *(ys[-1] + k3)))

        ys.append(ys[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    return ys


x = var("x")
Y = []


order = int(input("Enter order of the equation: "))

Y.append(var("y"))
for i in range(1, order + 1):
    Y.append(var("y" + str(i)))


func = (
    "y"
    + str(order)
    + " = "
    + "f(x, y, "
    + ", ".join(["y" + str(i) for i in range(1, order)])
    + ")"
)
user_input = input(f"Enter {func} =  ")
expr = simplify(user_input)

derv_Y = []
for i in range(1, len(Y) - 1):
    derv_Y.append(Y[i])

derv_Y.append(expr)

f = lambdify([x, *Y[:-1]], derv_Y)


eph = float(input("Enter the value of acceptable error: "))

a, b, h, cond_a, cond_b = getInput()


if cond_a[1] == 0 and cond_a[0] != 0:
    y_a = cond_a[2] / cond_a[0]
    y1_a_1 = float(input("Enter the first guess: ")) or np.random.rand()

    res_1 = rk4(f, [y_a, y1_a_1], a, b, h)
    err_1 = abs(cond_b[0] * res_1[-1][0] + cond_b[1] * res_1[-1][1] - cond_b[2])

    y1_a_2 = float(input("Enter the second guess: ")) or np.random.rand()
    res_2 = rk4(f, [y_a, y1_a_2], a, b, h)
    err_2 = abs(cond_b[0] * res_2[-1][0] + cond_b[1] * res_2[-1][1] - cond_b[2])

    while err_1 == err_2:
        y1_a_2 = np.random.rand()
        res_2 = rk4(f, [y_a, y1_a_2], a, b, h)
        err_2 = abs(cond_b[0] * res_2[-1][0] + cond_b[1] * res_2[-1][1] - cond_b[2])

    if err_2 < err_1:
        res = res_2
    else:
        res = res_1

    while min(err_1, err_2) > eph:
        y1_a_2 = y1_a_2 - ((y1_a_2 - y1_a_1) / (err_2 - err_1)) * err_2
        err_1 = err_2

        res = rk4(f, [y_a, y1_a_2], a, b, h)
        err_2 = abs(cond_b[0] * res[-1][0] + cond_b[1] * res[-1][1] - cond_b[2])


elif cond_a[0] == 0 and cond_a[1] != 0:
    y1_a = cond_a[2] / cond_a[1]
    y_a_1 = float(input("Enter the first guess: ")) or np.random.rand()

    res_1 = rk4(f, [y_a_1, y1_a], a, b, h)
    err_1 = abs(cond_b[0] * res_1[-1][0] + cond_b[1] * res_1[-1][1] - cond_b[2])

    y_a_2 = float(input("Enter the second guess: ")) or np.random.rand()
    res_2 = rk4(f, [y_a_2, y1_a], a, b, h)
    err_2 = abs(cond_b[0] * res_2[-1][0] + cond_b[1] * res_2[-1][1] - cond_b[2])

    if err_2 < err_1:
        res = res_2
    else:
        res = res_1

    while max(err_1, err_2) > eph:
        y_a_2 = y_a_2 - ((y_a_2 - y_a_1) / (err_2 - err_1)) * err_2
        err_1 = err_2

        res = rk4(f, [y_a_2, y1_a], a, b, h)
        err_2 = abs(cond_b[0] * res[-1][0] + cond_b[1] * res[-1][1] - cond_b[2])

else:
    y_a_1 = float(input("Enter the first guess: ")) or np.random.rand()
    y1_a_1 = (cond_a[2] - y_a_1 * cond_a[0]) / cond_a[1]

    res_1 = rk4(f, [y_a_1, y1_a_1], a, b, h)
    err_1 = abs(cond_b[0] * res_1[-1][0] + cond_b[1] * res_1[-1][1] - cond_b[2])

    y_a_2 = float(input("Enter the second guess: ")) or np.random.rand()
    y1_a_2 = (cond_a[2] - y_a_2 * cond_a[0]) / cond_a[1]

    res_2 = rk4(f, [y_a_1, y1_a_2], a, b, h)
    err_2 = abs(cond_b[0] * res_2[-1][0] + cond_b[1] * res_2[-1][1] - cond_b[2])

    if err_2 < err_1:
        res = res_2
    else:
        res = res_1

    while min(err_1, err_2) > eph:
        y1_a_2 = y1_a_2 - ((y1_a_2 - y1_a_1) / (err_2 - err_1)) * err_2
        err_1 = err_2

        res = rk4(f, [y_a_2, y1_a_2], a, b, h)
        err_2 = abs(cond_b[0] * res[-1][0] + cond_b[1] * res[-1][1] - cond_b[2])

print(res)
