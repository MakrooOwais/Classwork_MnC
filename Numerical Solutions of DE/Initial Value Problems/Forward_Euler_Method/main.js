const f_1 = (x, y) => {
    // Function f_1: Defines a simple mathematical function 2x + y and returns the result.
    // Parameters:
    //     x (float): The input value for variable x.
    //     y (float): The input value for variable y.
    // Returns:
    //     float: The result of the function 2x + y.
    return 2 * x + y;
};

const forward_euler = (f, h, a, b, y_a) => {
    // Function forward_euler: Implements the forward Euler method for solving a first-order ordinary differential equation (ODE).
    // Parameters:
    //     f (callable): The function representing the first-order ODE dy/dx = f(x, y).
    //     h (float): The step size for discretizing the interval [a, b].
    //     a (float): The initial value of x.
    //     b (float): The final value of x.
    //     y_a (float): The initial value of y at x = a.
    // Returns:
    //     list[float]: A list containing the approximate values of y for each step of the Euler method.
    n = Number((b - a) / h);
    results = Array(n).fill(0);

    results[0] = y_a;

    for (let i = 1; i < n; i++) {
        results[i] = results[i - 1] + h * f(a + (i - 1) * h, results[i - 1]);
    }

    return results;
};


// Main Program:
// - The main program uses the forward Euler method to approximate the solution of the first-order ODE dy/dx = 2x + y.
// - The `forward_euler` function is called with the provided parameters to obtain the approximate values of y.
// - The `print` function is used to display the list of approximate values of y at different steps of the Euler method.
console.log(forward_euler(f_1, 0.2, 0, 1, 1))
