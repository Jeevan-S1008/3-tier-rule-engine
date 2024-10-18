import unittest
from backend.rule_engine import parse_rule, evaluate_ast

class TestRuleEngine(unittest.TestCase):
    def test_parse_rule(self):
        rule = "age > 30 AND salary > 50000"
        ast = parse_rule(rule)
        self.assertIsNotNone(ast)

    def test_evaluate_ast(self):
        ast = parse_rule("age > 30 AND salary > 50000")
        data = {"age": 35, "salary": 60000}
        result = evaluate_ast(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
