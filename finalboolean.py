import ast

def translate_expression(node):
    if isinstance(node, ast.BoolOp):
        if isinstance(node.op, ast.And):
            return '(and {} {})'.format(
                translate_expression(node.values[0]),
                translate_expression(node.values[1])
            )
        elif isinstance(node.op, ast.Or):
            return '(or {} {})'.format(
                translate_expression(node.values[0]),
                translate_expression(node.values[1])
            )
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return '(not {})'.format(translate_expression(node.operand))
    elif isinstance(node, ast.NameConstant):
        return str(node.value).lower()

    raise ValueError('Invalid syntax.')

def translate_python_to_clojure(expression):
    parsed_expression = ast.parse(expression, mode='eval')
    return translate_expression(parsed_expression.body)

expression = 'not (False and True)'
clojure_expression = translate_python_to_clojure(expression)
print(clojure_expression)  # Resultado: (not (and true false))

