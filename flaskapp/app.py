from flask import Flask
from math import sin
app = Flask(__name__)

@app.route("/numericalintegralservice/<lower>/<upper>")
def numerical_integral(lower, upper):
    N = [10, 100, 1000, 10000, 100000, 1000000]
    integrals = []
    for n in N:
        I = 0.0
        dx = (float(upper) - float(lower)) / n
        for i in range(n):
            dI = eval(float(lower) + dx*(i + 0.5)) * dx
            I += dI
        integrals.append(I)
    results = ''
    for i, n in enumerate(N):
        results += f'<p>N = {n}: {integrals[i]}</p>\n'
    return results

def eval(x):
    return abs(sin(x))