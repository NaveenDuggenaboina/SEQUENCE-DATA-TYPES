import math
import numpy as np
import sympy as sp

# Basic arithmetic

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

# Trigonometry helpers

def trig_func(name, x, mode='radians'):
    if mode == 'degrees':
        x = math.radians(x)
    funcs = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
    }
    if name not in funcs:
        raise ValueError('Unsupported trig function')
    return funcs[name](x)

# Log / exp

def log_exp(op, x, base=10.0):
    if op == 'exp':
        return math.exp(x)
    if op in ('log', 'log10'):
        if x <= 0:
            raise ValueError('Log undefined for non-positive values')
        if op == 'log10':
            return math.log10(x)
        return math.log(x, base)
    if op == 'ln':
        if x <= 0:
            raise ValueError('Ln undefined for non-positive values')
        return math.log(x)
    raise ValueError('Unsupported operation')

# Complex ops

def complex_ops(op, a: complex, b: complex = 0+0j):
    if op == 'add':
        return a + b
    if op == 'sub':
        return a - b
    if op == 'mul':
        return a * b
    if op == 'div':
        return a / b
    if op == 'abs':
        return abs(a)
    if op == 'conjugate':
        return a.conjugate()
    raise ValueError('Unsupported complex op')

# Matrix parsing and operations

def parse_matrix(text: str) -> np.ndarray:
    # rows separated by ;, values by ,
    rows = [r.strip() for r in text.strip().split(';') if r.strip()]
    mat = [ [float(c) for c in row.split(',')] for row in rows ]
    return np.array(mat, dtype=float)


def matrix_ops(op: str, A: np.ndarray, B: np.ndarray = None):
    if op == 'add':
        if B is None:
            raise ValueError('B required')
        return A + B
    if op == 'mul':
        if B is None:
            raise ValueError('B required')
        return A.dot(B)
    if op == 'inverse A':
        return np.linalg.inv(A)
    if op == 'determinant A':
        return float(np.linalg.det(A))
    raise ValueError('Unsupported matrix op')

# Symbolic

x = sp.symbols('x')

def symbolic_derivative(expr_str: str):
    expr = sp.sympify(expr_str)
    return sp.diff(expr, x)


def symbolic_integral(expr_str: str):
    expr = sp.sympify(expr_str)
    return sp.integrate(expr, x)


# Quadratic solver
def quadratic_solver(a: float, b: float, c: float):
    """Return the roots of ax^2 + bx + c = 0.

    Returns a tuple (r1, r2) where r1 and r2 may be real or complex floats.
    """
    if a == 0:
        # linear equation bx + c = 0
        if b == 0:
            raise ValueError("Not an equation (a and b both zero)")
        return (-c / b, )
    disc = b * b - 4 * a * c
    if disc >= 0:
        sqrt_d = math.sqrt(disc)
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
        return (r1, r2)
    else:
        # complex roots
        sqrt_d = complex(0, math.sqrt(-disc))
        r1 = complex(-b, 0) + sqrt_d
        r1 = r1 / (2 * a)
        r2 = complex(-b, 0) - sqrt_d
        r2 = r2 / (2 * a)
        return (r1, r2)
