def f(x: float, y: float):
    return (2 - y**2) / (5 * x)


def f(x: float, y: float):
    return 1 + y * y


class MilnePreCorr:
    def __init__(self) -> None:
        self.param = {
            "h": None,
            "a": None,
            "b": None,
            "y_a": None,
            "error": 10e-3,
        }

    def set_param(self, a: float, b: float, h: float, y_a: float, error: float = None):
        self.param["h"] = h
        self.param["a"] = a
        self.param["b"] = b
        self.param["y_a"] = y_a
        self.param["error"] = error or self.param.get("error")

    def getFirstFour(self, f: callable):
        x = self.param.get
        h, a, y_a, error = x("h"), x("a"), x("y_a"), x("error")

        ys = []
        ys.append(y_a)
        for i in range(0, 3):
            ys.append(round(ys[i] + h * f(a + (i + 1) * h, ys[i]), len(str(error))))

        self.param["ys"] = ys

    def milnePred(self, f: callable, i: int):
        x = self.param.get
        h, a, ys = x("h"), x("a"), x("ys")
        return (
            ys[i - 3]
            + 4
            * h
            * (
                2 * f(a + h, ys[i - 2])
                - f(a + 2 * h, ys[i - 1])
                + 2 * f(a + 3 * h, ys[i])
            )
            / 3
        )

    def solve(self, f: callable):
        x = self.param.get
        self.getFirstFour(f)
        h, a, b, ys, error = x("h"), x("a"), x("b"), x("ys"), x("error")

        for i in range(3, int((b - a) / h)):
            y_old = self.milnePred(f, i)
            y_new = (
                ys[i - 1]
                + h
                * (
                    f(a + 2 * h, ys[i - 1])
                    + 4 * f(a + 3 * h, ys[i])
                    + f(a + 4 * h, y_old)
                )
                / 3
            )

            while abs(y_new - y_old) > error:
                y_old = y_new
                y_new = (
                    ys[2]
                    + h
                    * (
                        f(a + 2 * h, ys[2])
                        + 4 * f(a + 3 * h, ys[3])
                        + f(a + 4 * h, y_new)
                    )
                    / 3
                )

            ys.append(round(y_new, len(str(error))))

        return ys


# func = MilnePreCorr()
# func.set_param(0, 0.8, 0.2, 0)
# ys = func.getFirstFour(f)
# print(ys)

# print(func.solve(f))
