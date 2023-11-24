from sympy import *

# Make it pretty
init_printing(use_unicode=True)

x, y = symbols('x y')


def doubleintegral(func, x1, x2, y1, y2, order):
    if order == 'dxdy':
        integral_one = integrate(func, x)
        temp = simplify(integral_one.subs(x, x2)-integral_one.subs(x, x1))
        integral_two = integrate(temp, y)
        return simplify(integral_two.subs(y, y2)-integral_two.subs(y, y1))
    if order == 'dydx':
        integral_one = integrate(func, y)
        temp = simplify(integral_one.subs(y, y2) - integral_one.subs(y, y1))
        integral_two = integrate(temp, x)
        return simplify(integral_two.subs(x, x2) - integral_two.subs(x, x1))
    if order == 'polar':
        integral_one = integrate(func*x, x)
        temp = simplify(integral_one.subs(x, x2) - integral_one.subs(x, x1))
        integral_two = integrate(temp, y)
        return simplify(integral_two.subs(y, y2) - integral_two.subs(y, y1))
