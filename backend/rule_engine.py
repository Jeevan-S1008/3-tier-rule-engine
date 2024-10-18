import ast 

def parse_rule(rule_string):
    """Parses a rule string and generates an AST."""
    tokens = rule_string.split() 
    return create_ast_from_tokens(tokens)

def create_ast_from_tokens(tokens):
    """A simple recursive parser for creating an AST from tokens."""
    if len(tokens) == 1:
        return Node('operand', value=tokens[0])

    if 'AND' in tokens:
        operator_index = tokens.index('AND')
        left_tokens = tokens[:operator_index]
        right_tokens = tokens[operator_index + 1:]
        return Node(
            'operator',
            value='AND',
            left=create_ast_from_tokens(left_tokens),
            right=create_ast_from_tokens(right_tokens)
        )
  
    if 'OR' in tokens:
        operator_index = tokens.index('OR')
        left_tokens = tokens[:operator_index]
        right_tokens = tokens[operator_index + 1:]
        return Node(
            'operator',
            value='OR',
            left=create_ast_from_tokens(left_tokens),
            right=create_ast_from_tokens(right_tokens)
        )

def evaluate_ast(node, data):
    """Recursively evaluates the AST against provided user data."""
    if node.type == 'operand':
        return eval_condition(node.value, data)
    
    left_result = evaluate_ast(node.left, data)
    right_result = evaluate_ast(node.right, data)
      
    if node.value == 'AND':
        return left_result and right_result
    elif node.value == 'OR':
        return left_result or right_result

def eval_condition(condition, data):
    """Evaluates a single condition."""
    # This is just a placeholder; you need to implement proper condition parsing
    return eval(condition.format(**data))
