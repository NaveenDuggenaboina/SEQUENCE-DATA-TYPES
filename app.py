import streamlit as st
import numpy as np
from utils import (
    add, subtract, multiply, divide,
    trig_func, log_exp, complex_ops,
    parse_matrix, matrix_ops, symbolic_derivative, symbolic_integral,
    quadratic_solver,
)

st.set_page_config(page_title="Scientific Calculator", layout="wide")

st.title("Scientific Calculator — Streamlit")
st.write("Type of calculation on the left. Inputs and results on the right.")

calc_type = st.sidebar.selectbox("Calculation type", [
    "Basic Arithmetic",
    "Trigonometry",
    "Log / Exp",
    "Complex Numbers",
    "Matrix Operations",
    "Quadratic Solver",
    "Symbolic (SymPy)",
])

# Basic Arithmetic
if calc_type == "Basic Arithmetic":
    st.header("Basic Arithmetic")
    a = st.number_input("A", value=1.0, format="%.10g")
    b = st.number_input("B", value=2.0, format="%.10g")
    op = st.selectbox("Operator", ["+", "-", "*", "/"]) 
    if st.button("Compute"):
        try:
            if op == "+":
                res = add(a, b)
            elif op == "-":
                res = subtract(a, b)
            elif op == "*":
                res = multiply(a, b)
            else:
                res = divide(a, b)
            st.success(f"Result: {res}")
        except Exception as e:
            st.error(e)

# Trigonometry
elif calc_type == "Trigonometry":
    st.header("Trigonometric Functions")
    mode = st.radio("Angle mode", ["radians", "degrees"]) 
    func = st.selectbox("Function", ["sin", "cos", "tan"]) 
    x = st.number_input("Value", value=0.0, format="%.10g")
    if st.button("Evaluate"):
        res = trig_func(func, x, mode=mode)
        st.success(f"{func}({x} [{mode}] ) = {res}")

# Log / Exp
elif calc_type == "Log / Exp":
    st.header("Logarithms and Exponentials")
    op = st.selectbox("Operation", ["log", "ln", "exp", "log10"]) 
    x = st.number_input("Value", value=1.0, format="%.10g")
    base = st.number_input("Base (for log)", value=10.0, format="%.10g")
    if st.button("Compute"):
        try:
            res = log_exp(op, x, base=base)
            st.success(f"Result: {res}")
        except Exception as e:
            st.error(e)

# Complex Numbers
elif calc_type == "Complex Numbers":
    st.header("Complex number operations")
    a = st.text_input("First complex (e.g. 1+2j)", value="1+2j")
    b = st.text_input("Second complex (e.g. 3-4j)", value="3-1j")
    op = st.selectbox("Operator", ["add", "sub", "mul", "div", "abs", "conjugate"]) 
    if st.button("Run"):
        try:
            ca = complex(a.replace(' ', ''))
            cb = complex(b.replace(' ', ''))
            res = complex_ops(op, ca, cb)
            st.success(f"Result: {res}")
        except Exception as e:
            st.error(e)

# Matrix Operations
elif calc_type == "Matrix Operations":
    st.header("Matrix operations (enter rows as comma-separated numbers; rows separated by semicolon)")
    m1_txt = st.text_area("Matrix A", value="1,2;3,4")
    m2_txt = st.text_area("Matrix B (for binary ops)", value="5,6;7,8")
    op = st.selectbox("Operation", ["add", "mul", "inverse A", "determinant A"]) 
    if st.button("Compute"):
        try:
            A = parse_matrix(m1_txt)
            B = parse_matrix(m2_txt)
            res = matrix_ops(op, A, B)
            st.write("Result:")
            st.write(res)
        except Exception as e:
            st.error(e)

# Quadratic Solver
elif calc_type == "Quadratic Solver":
    st.header("Quadratic equation solver: ax^2 + bx + c = 0")
    a = st.number_input("a", value=1.0, format="%.10g")
    b = st.number_input("b", value=0.0, format="%.10g")
    c = st.number_input("c", value=0.0, format="%.10g")
    if st.button("Solve"):
        try:
            roots = quadratic_solver(a, b, c)
            if len(roots) == 1:
                st.success(f"Linear solution: x = {roots[0]}")
            else:
                st.success(f"Roots: x1 = {roots[0]}, x2 = {roots[1]}")
                disc = b * b - 4 * a * c
                st.write(f"Discriminant = {disc}")
                st.write("Type: " + ("real" if disc >= 0 else "complex"))
        except Exception as e:
            st.error(e)

# Symbolic
elif calc_type == "Symbolic (SymPy)":
    st.header("Symbolic operations with SymPy")
    expr = st.text_input("Expression (use x as variable)", value="x**2 + 3*x + 1")
    action = st.selectbox("Action", ["derivative", "integral"]) 
    point = st.number_input("Numeric evaluation point (optional)", value=float('nan'))
    if st.button("Compute"):
        try:
            if action == "derivative":
                res = symbolic_derivative(expr)
            else:
                res = symbolic_integral(expr)
            st.write("Symbolic result:")
            st.latex(str(res))
            if not np.isnan(point):
                val = res.subs({'x': point}) if hasattr(res, 'subs') else float(res)
                st.write(f"Numeric evaluation at x={point}: {float(val)}")
        except Exception as e:
            st.error(e)

st.markdown("---")
st.markdown("Built with Streamlit, NumPy and SymPy. See README for run instructions.")
