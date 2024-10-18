from flask import Flask, request, jsonify

from backend.ast import Node
from backend.rule_engine import parse_rule, evaluate_ast

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')
    ast = parse_rule(rule_string)
    return jsonify({'ast': repr(ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast_data = request.json.get('ast')
    data = request.json.get('data')
    result = evaluate_ast(ast_data, data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
