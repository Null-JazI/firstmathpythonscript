from sympy import symbols, nsolve, lambdify
import numpy as np
import matplotlib.pyplot as plt

# Define the variable
x = symbols('x')

# Ask the user for the equation input
equation_input = input("Enter the equation (in terms of x, e.g., 2*x**3 + 3*x - 1): ")

# Parse the input into a sympy expression
equation = eval(equation_input)

# Solve the equation numerically
approx_solution = nsolve(equation, x, 0)  # Initial guess at 0

print(f"The numerical solution is: {approx_solution}")

# Ask the user if they want to see the graph
show_graph = input("Would you like to see a graph of the function? (y/n): ")

if show_graph.lower() == 'y':
    # Convert the sympy equation to a numerical function for plotting
    f = lambdify(x, equation, "numpy")

    # Define the range for the graph
    x_vals = np.linspace(float(approx_solution) - 1, float(approx_solution) + 1, 400)
    y_vals = f(x_vals)

    # Plot the function
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=equation_input)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(float(approx_solution), color='red', linestyle='--', label=f'Solution at x ≈ {float(approx_solution):.3f}')
    plt.title("Graph of the Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
