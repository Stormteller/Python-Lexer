from tokens.tokens_enum import Tokens_Enum

def init_relop_FA():
    def relop_transition(state, symbol):
        if state == '0':
            if symbol == '<':
                return '1'
            if symbol == '=':
                return '2'
            if symbol == '>':
                return '3'
            if symbol == '!':
                return '4'
        if state == '1':
            if symbol == '=':
                return Tokens_Enum.LTE
            else:
                return Tokens_Enum.LT
        if state == '2':
            if symbol == '=':
                return Tokens_Enum.EQ
            else:
                return Tokens_Enum.ASSIGN
        if state == '3':
            if symbol == '=':
                return Tokens_Enum.GTE
            else:
                return Tokens_Enum.GT
        if state == '4':
            if symbol == '=':
                return Tokens_Enum.NOT_EQ

    relop_accepting = [
        Tokens_Enum.GT,
        Tokens_Enum.GTE,
        Tokens_Enum.LT,
        Tokens_Enum.LTE,
        Tokens_Enum.EQ,
        Tokens_Enum.ASSIGN
    ]

    return '0', relop_transition, relop_accepting