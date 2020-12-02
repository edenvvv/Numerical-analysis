import numpy
from numpy import log as ln


# Defining Function
def f(x):
    return x ** 4 + x ** 3 - 3*x ** 2


# Implementing Bisection Method
def bisection_method(a, b, e):
    # add check error blob
    if f(a) * f(b) > 0.0:
        print('Try Again with different guess values')
    else:
        stop = - ln(e/(b-a))/ln(2)
        step = 1
        condition = True
        while condition:
            if step > stop:
                print("The method is not suitable")
                exit(0)
            m = (a + b) / 2
            print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))

            if f(a) * f(m) < 0:
                b = m
            else:
                a = m

            step += 1
            condition = abs(f(m)) > e

        print('\nRequired Root is : %0.5f' % m)


# main
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = 0.0001

# Checking Correctness of initial guess values and bisecting
bisection_method(a, b, e)
