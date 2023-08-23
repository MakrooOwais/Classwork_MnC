# Runge-Kutta Method Implementation Using Classes - Explanation

The provided code implements the **Runge-Kutta method** for solving ordinary differential equations (ODEs) using a class-based approach. Let's break down the code and understand how classes are utilized to implement this numerical technique.

## Class `RungeKuttaMethod`

This class represents the core of the Runge-Kutta method implementation. It contains methods and attributes necessary for solving ODEs numerically.

### Class Attributes

- `coefficients_dict`: A dictionary containing coefficients for different orders of the Runge-Kutta method.
- `coefficients_k_dict`: A dictionary containing coefficients for evaluating `k_i` values.
- `order`: The order of the Runge-Kutta method.
- `result`: The final result of the method.
- `k_i`: A list to store intermediate values.

### Constructor `__init__(self, order: int)`

The constructor initializes the class instance with the specified order and creates placeholders for the result and `k_i` values.

### Method `solve(self, f: callable, a: float, y_a: float, h: float) -> float`

This method is responsible for solving the given ODE using the Runge-Kutta method. It takes the following inputs:

- `f`: The callable representing the differential equation.
- `a`: The initial value of the independent variable.
- `y_a`: The initial value of the dependent variable at `a`.
- `h`: The step size.

Inside the method:

1. The appropriate coefficients are retrieved based on the order of the method.
2. The `k_i` values are calculated using the provided differential equation and coefficients.
3. The final result is computed by combining the weighted `k_i` values.
4. The result is rounded to ensure precision.

### Method `getKs(self) -> list`

This method returns the list of intermediate `k_i` values.

## Creating Instances and Solving Equations

Three instances of the `RungeKuttaMethod` class are created for orders 2, 3, and 4. The equations `f_1` and `f_2` are solved using each instance with different initial conditions and step sizes.

## Benefits of Using Classes

1. **Modularity**: The class-based approach encapsulates the implementation details within the class, making the code more modular and organized.
2. **Reusability**: Once the class is defined, it can be reused to solve various ODEs with different initial conditions and orders.
3. **Readability**: The use of classes improves code readability by grouping related functionality together.

## Conclusion

By using classes to implement the Runge-Kutta method, the code becomes more structured, reusable, and maintainable. This approach is particularly beneficial when dealing with multiple orders of the method and varying differential equations, as it allows for a clear separation of concerns and efficient code management.
