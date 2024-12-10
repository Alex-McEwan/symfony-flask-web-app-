import flask
from flask import request, jsonify
import matplotlib.pyplot as plt
import io
import base64
import sympy 
import numpy as np 

app = flask.Flask(__name__)



def generate_plot(function_string, title):
        print("THE FUNCTION IS", function_string, "THE TITLE IS:", title)

        func_symbol = sympy.sympify(function_string)
        variables = func_symbol.free_symbols
        if not variables:
            dependent_variable = sympy.symbols("x")
        else: 
            dependent_variable = variables.pop()
        f = sympy.lambdify(dependent_variable, func_symbol)
        x = np.linspace(0, 10, 200)
        y = f(x)

        dependent_variable_str = str(dependent_variable)

        plt.figure()
        plt.plot(x, y, label=function_string)
        plt.legend()
        plt.xlabel(dependent_variable_str)
        plt.ylabel("y")
        plt.title(title)
        buf = io.BytesIO()
        plt.savefig(buf, format="jpeg")
        plt.savefig("migratie test.png" ,format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode("utf-8")
        buf.close()
        return image_base64      


def generate_plot3d(function_string, title):
    print("THE FUNCTION IS", function_string, "THE TITLE IS:", title)
    func_symbol = sympy.sympify(function_string)
    variables = func_symbol.free_symbols
    if len(variables) > 2:
        raise ValueError("more than 2 variables were entered") 
    
    elif len(variables) == 1:
        var = next(iter(variables))
        if str(var) != "x":
            dependent_variable1 = sympy.symbols("x")
            dependent_variable2 = var
            
        else: 
            dependent_variable1 = var
            dependent_variable2 = sympy.symbols("y")

    elif not variables:
        dependent_variable1 = sympy.symbols("x")
        dependent_variable2 = sympy.symbols("y")

    
    
    else: 
        dependent_variable1, dependent_variable2 = sorted(variables, key=lambda variable : str(variable))

    f = sympy.lambdify((dependent_variable1, dependent_variable2), func_symbol)
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)  
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap="viridis")
    ax.set_xlabel(str(dependent_variable1))
    ax.set_ylabel(str(dependent_variable2))
    ax.set_zlabel("z")
    ax.set_title(title)
    buf = io.BytesIO()
    plt.savefig(buf, format="jpeg")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    return image_base64



@app.route("/health")
def health_check():
    return "API is running", 200



@app.route("/plot", methods=["POST"])
def plot():
    try:        
        data = request.json
        function_str = data.get("function")
        title = data.get("title", "default title")
        image_base64 = generate_plot(function_str, title)

        return jsonify({"plot": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/plot3d", methods=["POST"])
def plot3d():
    try:        
        data = request.json
        function_str = data.get("function")
        title = data.get("title", "default title")
        image_base64 = generate_plot3d(function_str, title)

        return jsonify({"plot": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 

@app.route("/")
def home():
    return "hello world"





app.run(host="0.0.0.0", port=5000, debug=True)



