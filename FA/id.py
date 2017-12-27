from tokens.tokens_enum import Tokens_Enum

def init_id_FA():
    def id_transition(state, symbol):
        if state == '0':
            if (symbol.isalpha() or symbol == '_'):
                return '1'

        if state == '1':
            if (symbol.isalpha() or symbol.isdigit() or symbol == '_'):
                return '1'
            else:
                return Tokens_Enum.ID

    id_accepting = [
        Tokens_Enum.ID,
    ]

    return '0', id_transition, id_accepting