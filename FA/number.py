from tokens.tokens_enum import Tokens_Enum

def init_number_FA():
    def number_transition(state, symbol):
        if state == '0':
            if symbol.isdigit():
                return '1'
        if state == '1':
            if symbol.isdigit():
                return '1'
            elif symbol == '.':
                return '2'
            else:
                return Tokens_Enum.NUMBER
        if state == '2':
            if symbol.isdigit():
                return '3'
        if state == '3':
            if symbol.isdigit():
                return '3'
            else:
                return Tokens_Enum.NUMBER

    number_accepting = [
        Tokens_Enum.NUMBER
    ]

    return '0', number_transition, number_accepting