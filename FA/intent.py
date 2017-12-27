from tokens.tokens_enum import Tokens_Enum

def init_intent_FA():
    def intent_transition(state, symbol):
        if state == '0':
            if symbol == '\n':
                return '1'
        if state == '1':
            if symbol == ' ':
                return '2'
        if state == '2':
            if symbol == ' ':
                return '2'
            else:
                return Tokens_Enum.INTENT_SPACE

    intent_accepting = [
        Tokens_Enum.INTENT_SPACE,
    ]

    return '0', intent_transition, intent_accepting