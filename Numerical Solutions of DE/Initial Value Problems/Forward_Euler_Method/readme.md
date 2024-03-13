# Numerical Methods for Ordinary Differential Equations (ODEs)

This repository contains Python code implementing numerical methods for solving first-order Ordinary Differential Equations (ODEs). Ordinary Differential Equations are mathematical equations that involve the rate of change of a function with respect to a single independent variable. They find wide applications in various scientific and engineering disciplines to model dynamic systems and predict their behavior over time.

In this repository, we have implemented **Forward Euler Method** (`forward_euler` function) for solving first-order ODEs.

## Forward Euler Method

The Forward Euler method is a simple and widely-used numerical technique for approximating the solution of first-order ODEs. It discretizes the domain into equally spaced intervals and estimates the next value of the function based on the current value and the slope at that point. The method is explicit, meaning it directly estimates the value of the function at each step. The steps involved in the Forward Euler method are as follows:

1. **Define the ODE:** Start with a first-order ODE of the form `dy/dx = f(x, y)`, where `y` is the dependent variable and `x` is the independent variable. The function `f(x, y)` represents the rate of change or the slope of the function at each point.

2. **Discretize the Domain:** Choose a step size `h` and divide the interval `[a, b]` into equally spaced points. The smaller the step size, the more accurate the approximation, but it also increases the computational cost.

3. **Initial Condition:** Set the initial value of `y` at the starting point `x = a`. This is often referred to as the initial condition `y_a`.

4. **Approximate `y`:** Use the Forward Euler method to approximate the value of `y` at each step:

    ```text
    y_(i+1) = y_i + h * f(x_i, y_i)
    ```

    where `y_i` is the current approximation of `y` at `x = x_i`, and `y_(i+1)` is the next approximation at `x = x_i + h`.

5. **Output:** The final list of approximate values of `y` represents an approximate solution to the given ODE over the interval `[a, b]`.

The Forward Euler method is relatively straightforward to implement, making it a suitable starting point for solving ODEs numerically. However, it has its limitations, such as numerical instability for large step sizes and limited accuracy for long intervals.

## Conclusion

Numerical methods for solving ODEs are powerful tools to approximate the behavior of dynamic systems when analytical solutions are not feasible or too complex to obtain. The Forward Euler method and Breadth-First Search algorithm are just two examples of the numerous numerical techniques used in various fields of science, engineering, and computer science.

We hope that this repository and the explanations provided here will serve as a valuable resource for understanding and implementing these numerical methods to solve first-order ODEs and graph-related problems. Feel free to explore the Python code and use it in your projects or studies. If you have any questions or suggestions, please do not hesitate to reach out.

Happy coding!
