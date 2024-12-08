import flask
from flask import request, jsonify
import matplotlib.pyplot as plt
import io
import base64
import sympy 
import numpy as np 

app = flask.Flask(__name__)

@app.route("/health")
def health_check():
    return "API is running", 200



@app.route("/plot", methods=["POST"])
def plot():
    try:        
        data = request.json
        function_str = data.get("function")
        title = data.get("title", "default title")
        print("THE FUNCTION IS", function_str, "THE TITLE IS:", title)
        if not function_str:
            return jsonify({"error": "Function is required"}), 400

        func_symbol = sympy.sympify(function_str)
        variables = func_symbol.free_symbols
        if not variables:
            dependent_variable = sympy.symbols("x")
        else: 
            dependent_variable = variables.pop()
        f = sympy.lambdify(dependent_variable, func_symbol)
        x = np.linspace(-10, 10, 200)
        y = f(x)

        dependent_variable_str = str(dependent_variable)

        plt.figure()
        plt.plot(x, y, label=function_str)
        plt.legend()
        plt.xlabel(dependent_variable_str)
        plt.ylabel("y")
        plt.title(title)
        buf = io.BytesIO()
        plt.savefig(buf, format="jpeg")
        
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode("utf-8")
        buf.close()

        return jsonify({"plot": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return "hello world"

app.run(host="0.0.0.0", port=5000, debug=True)



def generate_plot(function_string):
        func_symbol = sympy.sympify(function_string)
        variables = func_symbol.free_symbols
        dependent_variable = variables.pop()
        dependent_variable_str = sympy.srepr(dependent_variable)

        f = sympy.lambdify(dependent_variable, func_symbol)
        x = np.linspace(-10, 10, 200)
        y = f(x)    
        plt.figure()
        plt.plot(x, y, label=function_string)
        plt.legend()
        plt.xlabel(dependent_variable_str)
        plt.ylabel("y")
        plt.title("Generated Plot")


