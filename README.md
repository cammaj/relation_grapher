# relation_grapher

A small Python program that visualizes binary relations on a finite set as a directed graph.

Features
- Define a set S (by default integers from -3 to 3).
- Provide a relation condition using variables `x` and `y` (Python expression) or press ENTER to use the default relation.
- Visualize the relation as a directed graph using NetworkX and Matplotlib.

Default relation
- (x - y) % 2 == 0 — pairs with the same parity.

Usage
1. Install dependencies (recommended to use a virtual environment):

   pip install -r requirements.txt

2. Run the program:

   python main.py

3. When prompted, enter a Python boolean expression using `x` and `y`.
   - Example inputs:
     - `x == y` (identity relation)
     - `x < y` (strict order)
     - `(x - y) % 2 == 0` (same parity) — the default

Notes
- The program evaluates the expression with Python's `eval()` for each pair (x, y) in S × S. Use `==` for equality, logical operators (`and`, `or`, `not`), comparison operators (`<`, `>`, `<=`, `>=`), arithmetic, and modulo as needed.
- Be careful with malformed input — the program will report an evaluation error and exit.

Files
- `main.py` — main program
- `requirements.txt` — Python dependencies

License
See the LICENSE file.

2026 © Kamil Gzyl [cammaj]
