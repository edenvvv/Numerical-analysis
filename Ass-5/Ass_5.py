# eden dadon id:207279183
# Eliran Dagan id: 208061580
from scipy import misc

def f(x):
    return 4*x ** 3 - 48*x + 5

def newton_method(x0, x1, eps):
    step = 0
    min = x0
    max = x1
    xn = x0

    while True:
        fxn = f(xn)
        if abs(fxn) < eps:
            print(f"range: [{min} ,{max}]: in {step} iterations: {xn}")
            break
        f_derivative = misc.derivative(f, xn)
        if f_derivative == 0:
            print("No solution found.")
            break
        xn = xn - fxn/f_derivative
        step += 1


def secant_method(x0, x1, e):
    min = x0
    max = x1
    step = 1
    runner = True

    while runner:
        if f(x0) == f(x1):
            print("Divide by zero")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        step += 1

        runner = abs(f(x2)) > e
    print(f"range: [{min} ,{max}]: in {step} iterations: {x2}")


# main
epsilon = 0.0001
min_range = int(input("enter min: "))
max_range = int(input("enter max: "))
newton_ranges = []
secant_ranges = []

for i in range(min_range, max_range):
    if f(i) * f(i + 1) < 0:
        newton_ranges.append((i, i + 1))
        secant_ranges.append((i, i + 1))

print("* Newton-Raphson method:")

if len(newton_ranges) == 0:
    print("The function does not match the Newton Raphson method")
else:
    for ranges in newton_ranges:
        newton_method(ranges[0], ranges[1], epsilon)

print("* secant method:")

if len(secant_ranges) == 0:
    print("The function does not match the secant method")
else:
    for ranges in secant_ranges:
        secant_method(ranges[0], ranges[1], epsilon)
