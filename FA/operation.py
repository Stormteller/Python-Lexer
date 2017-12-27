from tokens.tokens_enum import Tokens_Enum

def init_operation_FA():
    def operation_transition(state, symbol):
        if state == '0':
            if symbol == '+':
                return '1'
            if symbol == '-':
                return '2'
            if symbol == '*':
                return '3'
            if symbol == '/':
                return '4'
        if state == '1':
            if symbol == '=':
                return Tokens_Enum.PLUS_EQ
            else:
                return Tokens_Enum.PLUS
        if state == '2':
            if symbol == '=':
                return Tokens_Enum.MINUS_EQ
            else:
                return Tokens_Enum.MINUS
        if state == '3':
            if symbol == '=':
                return Tokens_Enum.MULTIPLY_EQ
            elif symbol == '*':
                return Tokens_Enum.POWER
            else:
                return Tokens_Enum.MULTIPLY
        if state == '4':
            if symbol == '=':
                return Tokens_Enum.DIVIDE_EQ
            else:
                return Tokens_Enum.DIVIDE

    operation_accepting = [
        Tokens_Enum.PLUS,
        Tokens_Enum.PLUS_EQ,
        Tokens_Enum.MINUS,
        Tokens_Enum.MINUS_EQ,
        Tokens_Enum.MULTIPLY,
        Tokens_Enum.MULTIPLY_EQ,
        Tokens_Enum.DIVIDE,
        Tokens_Enum.DIVIDE_EQ,
        Tokens_Enum.POWER,
    ]

    return '0', operation_transition, operation_accepting