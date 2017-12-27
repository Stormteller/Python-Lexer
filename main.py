from python_lexer import PythonLexer

if __name__ == '__main__':
    lexer = PythonLexer()

    with open('to_parse.py', 'r') as parse_file:
        data = parse_file.read()
        try:
            tokens = lexer.tokenize(data)
            print(tokens)
        except ValueError as e:
            print(e)
