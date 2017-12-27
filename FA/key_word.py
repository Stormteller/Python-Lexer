from tokens.tokens_enum import Tokens_Enum




def init_key_word_FA(keyword, token):
    if not isinstance(token, Tokens_Enum):
        raise ValueError('Unsupported token')

    def keyword_transition(state, symbol):
        next_state = None
        if state == keyword and not symbol.isalpha() and not symbol.isdigit() and symbol != '_':
            return token

        if state == '0':
            if symbol == keyword[0]:
                next_state = keyword[0]
        elif keyword.startswith(state):
            if keyword.startswith(state + symbol):
                next_state = state + symbol
        return next_state


    keyword_accepting = [
        token
    ]

    return '0', keyword_transition, keyword_accepting