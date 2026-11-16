
# Gradient Descent Algorithm

# Define function
def f(x):
    return x*x + 4*x + 5

# Define derivative
def derivative(x):
    return 2*x + 4

# Take input
x = float(input("Initial x: "))
lr = float(input("Learning rate: "))
iterations = int(input("Number of iterations: "))

# Gradient Descent
for i in range(iterations):

    x = x - lr * derivative(x)

    print("Iteration", i+1, "x =", round(x, 4),
          "f(x) =", round(f(x), 4))

# Final result
print("\nMinimum x =", round(x, 4))
print("Minimum value =", round(f(x), 4))
