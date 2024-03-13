const f_1 = (x, y) => {
    return 2 * x + y;
};

const modFEM = (f, h, a, b, y_a) => {
    const n = (b - a) / h;

    results = Array(n).fill(0);
    results[0] = y_a;

    for (let i = 1; i < n; i++) {
        results[i] = results[i - 1] + h * f(a + (i - 1) * h, results[i - 1]);
        temp =
            results[i - 1] +
            (h / 2) *
                (f(a + (i - 1) * h, results[i - 1]) + f(a + i * h, results[i]));

        while (Math.abs(temp - results[i]) > 10e-5) {
            results[i] = temp;
            temp =
                results[i - 1] +
                (h / 2) *
                    (f(a + (i - 1) * h, results[i - 1]) +
                        f(a + i * h, results[i]));
        }

        results[i] = Math.round(results[i] * 10e4) / 10e4;
    }

    return results;
};

console.log(modFEM(f_1, 0.2, 0, 1, 1));
