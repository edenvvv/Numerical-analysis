# eden dadon id:207279183
# Eliran Dagan id: 208061580
import sympy as sp


def f(x):
    return x**4 + x**3 - 3*x**2


def derivative_of_f(x):
    return 4*x**3 + 3*x**2 - 6*x


def bisection_method(a, b, e, func):
    # add check error blob
    if func(a) * func(b) > 0.0:
        print('Try Again with different guess values')
    else:
        step = 1
        condition = True
        while condition:
            m = (a + b) / 2

            if func(a) * func(m) < 0:
                b = m
            else:
                a = m

            step += 1
            condition = abs(func(m)) > e

        if func.__name__ == "derivative_of_f":
            if f(round(m, 1)) == 0.0:
                result.append(m)
        else:
            result.append(m)


def max_range(min_range, max_range):
    segment = 0.1
    segment_list = []
    index = min_range

    while index <= max_range:
        segment_list.append(round(index, 1))
        index += segment
    segment_list.append(max_range)

    for inx, x in enumerate(segment_list):
        if inx < len(segment_list) - 1:

            if segment_list[inx+1] == 0:
                if inx < len(segment_list) - 2:

                    if f(x) * f(segment_list[inx + 2]) < 0.00:
                        bisection_method(x, segment_list[inx + 2], e, f)

                    if derivative_of_f(x) * derivative_of_f(segment_list[inx + 2]) < 0.00:
                        bisection_method(x, segment_list[inx + 2], e, derivative_of_f)

            if f(x) * f(segment_list[inx + 1]) < 0.00:
                bisection_method(x, segment_list[inx + 1], e, f)

            if derivative_of_f(x) * derivative_of_f(segment_list[inx + 1]) < 0.00:
                bisection_method(x, segment_list[inx + 1], e, derivative_of_f)


# main
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
result = []
e = 0.00001

max_range(a, b)
print("there roots are:")

for i in result:
    print("%0.5f" % i)
