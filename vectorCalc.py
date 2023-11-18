from sympy import *
from sympy.vector import *

# Make it pretty
init_printing(use_unicode=True)

t = symbols('t')


def out(sol):
    sol = sol.simplify()

    user_out = input("""If you want the LaTeX output please enter L, 
    if you want to evaluate enter E, 
    if you want the standard out enter S.
    """)

    if user_out == "L":
        print(latex(sol))
    if user_out == "S":
        print(sol)
    if user_out == "E":
        print(simplify(sol.subs(t, sympify(input("t=")))))
        print(sol.subs(t, sympify(input("t="))).evalf())


def curvature(x, y, z):
    N = CoordSys3D('N')
    r = x * N.i + y * N.j + z * N.k

    rdiff = diff(r, t)
    r2diff = diff(rdiff, t)

    sol = rdiff.cross(r2diff).magnitude() / rdiff.magnitude() ** 3

    return sol


def tangent(x, y, z):
    N = CoordSys3D('N')
    r = x * N.i + y * N.j + z * N.k
    rdiff = diff(r, t)

    sol = rdiff / rdiff.magnitude()

    return sol


def normal(x, y, z):
    T_prime = diff(tangent(x, y, z))

    return T_prime / T_prime.magnitude()


def binom(x, y, z):
    return tangent(x, y, z).cross(normal(x, y, z))


# Make the window here
def main():
    while True:
        print(
            """Select an operation from the following list: 
            (Curvature: k) 
            (Unit Tangent Vector: T)
            (Unit Normal Vector: N)
            (Unit Binomial Vector: B)"""
        )
        inpt = input("")

        expression = input("""Your curve please
        in the following format
        ***,***,***
        """)

        xyz = expression.split(",")
        x = sympify(xyz[0])
        y = sympify(xyz[1])
        z = sympify(xyz[2])

        if inpt == "k":
            try:
                out(curvature(x, y, z))
            except ValueError:
                print("Error Occurred")

        if inpt == "T":
            try:
                out(tangent(x, y, z))
            except ValueError:
                print("There is no Tangent Vector for the given curve.")

        if inpt == "N":
            try:
                out(normal(x, y, z))
            except ValueError:
                print("There is no Normal Vector for the given curve.")

        if inpt == "B":
            try:
                out(binom(x, y, z))
            except ValueError:
                print("There is no Binomial Vector for the given curve.")


main()
