import math
from utils import add, trig_func, symbolic_derivative


def test_add():
    assert add(1, 2) == 3


def test_trig_degrees():
    # sin(30 degrees) approx 0.5
    val = trig_func('sin', 30, mode='degrees')
    assert abs(val - 0.5) < 1e-9


def test_symbolic_derivative():
    d = symbolic_derivative('x**3')
    assert str(d) == '3*x**2'


def test_quadratic_solver_real_roots():
    from utils import quadratic_solver
    r1, r2 = quadratic_solver(1, -3, 2)  # x^2 -3x +2 = 0 => (1,2)
    assert {round(r1, 6), round(r2, 6)} == {1.0, 2.0}


def test_quadratic_solver_complex_roots():
    from utils import quadratic_solver
    r1, r2 = quadratic_solver(1, 0, 1)  # x^2 + 1 = 0 => i and -i
    # ensure complex conjugates
    assert complex(r1).conjugate() == complex(r2)
