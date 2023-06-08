import re

def lexer(expression):
    tokens = []
    pattern = r'\d+|\+|\-|\*|\/|\(|\)|[a-zA-Z_][a-zA-Z0-9_]*'
    token_regex = re.compile(pattern)
    matches = re.findall(token_regex, expression)

    for match in matches:
        if match.isdigit():
            tokens.append(('NUMBER', int(match)))
        elif match.isalpha():
            tokens.append(('VARIABLE', match))
        else:
            tokens.append(('OPERATOR', match))

    return tokens

def parser(tokens):
    pos = 0

    def parse_term():
        nonlocal pos
        left = parse_factor()

        while pos < len(tokens):
            token = tokens[pos]
            if token[0] == 'OPERATOR' and token[1] in ('*', '/'):
                pos += 1
                right = parse_factor()
                left = ('OPERATION', token[1], left, right)
            else:
                break

        return left

    def parse_expression():
        nonlocal pos
        left = parse_term()

        while pos < len(tokens):
            token = tokens[pos]
            if token[0] == 'OPERATOR' and token[1] in ('+', '-'):
                pos += 1
                right = parse_term()
                left = ('OPERATION', token[1], left, right)
            else:
                break

        return left

    def parse_factor():
        nonlocal pos
        token = tokens[pos]

        if token[0] == 'NUMBER':
            pos += 1
            return ('NUMBER', token[1])
        elif token[0] == 'VARIABLE':
            pos += 1
            return ('VARIABLE', token[1])
        elif token[0] == 'OPERATOR' and token[1] == '(':
            pos += 1
            result = parse_expression()
            pos += 1  # Skip closing parenthesis
            return result
        else:
            raise ValueError(f'Invalid token: {token}')

    return parse_expression()

def translate(ast):
    if ast[0] == 'NUMBER':
        return str(ast[1])
    elif ast[0] == 'VARIABLE':
        return ast[1]
    elif ast[0] == 'OPERATION':
        operator = ast[1]
        left = translate(ast[2])
        right = translate(ast[3])
        return f'({operator} {left} {right})'
    else:
        raise ValueError(f'Invalid AST node: {ast}')

def python_to_clojure(expression):
    tokens = lexer(expression)
    ast = parser(tokens)
    return translate(ast)

expressions = [
    '2 + 3 * 4',
    '2 * (3 + 4)',
    'x + y / z'
]

for expression in expressions:
    print(f'Python: {expression}')
    print(f'Clojure: {python_to_clojure(expression)}')
    print()
