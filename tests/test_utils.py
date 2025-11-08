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
