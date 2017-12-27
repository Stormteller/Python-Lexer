from tokens.tokens_enum import Tokens_Enum

def init_string_FA():
    def string_transition(state, symbol):
        if state == '0':
            if symbol == '"':
                return '1'
            if symbol == "'":
                return '2'
        if state == '1':
            if symbol == '"':
                return Tokens_Enum.STRING
            if symbol != '\n':
                return '1'
        if state == '2':
            if symbol == "'":
                return Tokens_Enum.STRING
            if symbol != '\n':
                return '2'

    string_accepting = [
        Tokens_Enum.STRING
    ]

    return '0', string_transition, string_accepting