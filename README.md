# Scientific Calculator — Streamlit

This repository contains a small Streamlit-based scientific calculator app implemented for Python 3.10-compatible packages.

Files added/updated:

- `app.py` — the Streamlit app UI and wiring (entry point)
- `utils.py` — calculation helpers (basic math, trig, matrix, complex, SymPy symbolic ops)
- `requirements.txt` — pinned packages compatible with Python 3.10
- `tests/test_utils.py` — minimal unit tests for key helpers

Quick start (Windows PowerShell):

```powershell
# create and activate a venv, install requirements, then run Streamlit
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; streamlit run app.py
```

Notes and features:

- Basic arithmetic (+, -, *, /) with error handling for division by zero.
- Trigonometric functions (sin, cos, tan) with radians/degrees mode.
- Logarithms, natural log, exponentials.
- Complex number operations (add/sub/mul/div/abs/conjugate).
- Matrix parsing (rows as comma-separated values; rows separated by semicolons) with addition, multiplication, inverse and determinant.
- Symbolic derivative and integral using SymPy with optional numeric evaluation.

Run tests locally (after creating/activating your venv and installing requirements):

```powershell
# activate venv then
# pip install -r requirements.txt
pytest -q
```

If package installation fails, try installing packages individually (for example `pip install streamlit sympy numpy scipy`) and ensure you're using Python 3.10.

If you want improvements (better matrix UI, more symbolic features, expression history, or keyboard-friendly inputs), tell me which area to expand next.

New example added:

- `Quadratic Solver` — available from the app sidebar. Enter coefficients a, b, c and it returns real or complex roots and the discriminant.