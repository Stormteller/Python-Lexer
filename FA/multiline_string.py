from tokens.tokens_enum import Tokens_Enum

def init_multiline_string_FA():
    def multiline_string_transition(state, symbol):
        if state == '0':
            if symbol == '"':
                return '1'
            if symbol == "'":
                return '2'
        if state == '1':
            if symbol == '"':
                return '3'
        if state == '2':
            if symbol == "'":
                return '4'
        if state == '3':
            if symbol == '"':
                return '5'
        if state == '4':
            if symbol == "'":
                return '6'

        if state == '5':
            if symbol != '"':
                return '5'
            else:
                return '7'
        if state == '6':
            if symbol != "'":
                return '6'
            else:
                return '8'

        if state == '7':
            if symbol == '"':
                return '9'
            else:
                return '5'
        if state == '8':
            if symbol == "'":
                return '10'
            else:
                return '6'
        if state == '9':
            if symbol == '"':
                return Tokens_Enum.MULTILINE_STRING
            else:
                return '5'
        if state == '10':
            if symbol == "'":
                return Tokens_Enum.MULTILINE_STRING
            else:
                return '6'



    multiline_string_accepting = [
        Tokens_Enum.MULTILINE_STRING
    ]

    return '0', multiline_string_transition, multiline_string_accepting