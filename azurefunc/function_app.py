import azure.functions as func
import logging
from flask import Flask
from math import sin

flask_app = Flask(__name__)

@flask_app.route("/numericalintegralservice/<lower>/<upper>")
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

app = func.WsgiFunctionApp(app=flask_app.wsgi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

# @app.route(route="numintegr_func")
# def numintegr_func(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )