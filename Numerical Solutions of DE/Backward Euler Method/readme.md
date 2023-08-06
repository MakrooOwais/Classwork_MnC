# Backward Euler Method for Solving First-Order Ordinary Differential Equations

The Backward Euler method is a numerical technique used to approximate the solution of first-order Ordinary Differential Equations (ODEs). It is an implicit method known for its stability, making it particularly useful for solving stiff ODEs where other explicit methods like the Forward Euler method may fail.

## Introduction

This Python code provides an implementation of the Backward Euler method to solve a first-order ODE of the form `dy/dx = f(x, y)`. The user needs to provide the ODE function `f(x, y)`, the interval `[a, b]`, the step size `h`, and the initial condition `y_a`. The code then approximates the values of `y` at each step within the interval.

## Mathematical Background

The Backward Euler method approximates the value of `y` at each step `x_i` using the following formula:

```python
y_i = nsolve(y - y_(i-1) - h * f(x_i, y), y, y_(i-1))
```

Here, `y_i` represents the current approximation of `y` at `x = x_i`, `y_(i-1)` is the previous approximation at `x = x_(i-1)`, `h` is the step size, and `nsolve` is a function from the `sympy` library used to solve the equation for `y_i`.

## Usage

1. Define the ODE function `f(x, y)` that represents the rate of change or the slope of the function at each point.

2. Specify the interval `[a, b]` over which the solution is required.

3. Choose a suitable step size `h`. Smaller step sizes yield more accurate results, but they increase the computational cost.

4. Set the initial condition `y_a` which represents the value of `y` at the starting point `x = a`.

5. Call the `backward_euler` function with the provided parameters to approximate the values of `y` at each step.

## Example

```python
import sympy as sp

# Define the ODE function dy/dx = 2*x + y
def f(x, y):
    return 2 * x + y

# Set the interval [a, b], step size h, and initial condition y_a
a = 0
b = 1
h = 0.2
y_a = 1

# Use the Backward Euler method to solve the ODE
results = backward_euler(f, a, b, h, y_a)

# Print the approximate values of y at each step
print(results)
```

## Dependencies

The code uses the `sympy` library to symbolically solve the equation at each step. Ensure that `sympy` is installed in your Python environment before running the code.

## Note

The accuracy of the Backward Euler method depends on the step size `h`. For complex ODEs or stiff systems, other numerical methods like the Runge-Kutta method or implicit methods may be more suitable. The user should experiment with different step sizes to achieve the desired level of accuracy.
