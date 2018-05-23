from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000},
    # {'description': '', 'amount': },

]

# Handle GET
@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

# Handle POST
@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

# OLD ONE
# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "Hello world"
