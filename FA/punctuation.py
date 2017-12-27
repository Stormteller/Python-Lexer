from tokens.tokens_enum import Tokens_Enum

def init_punctuation_FA():
    def punctuation_transition(state, symbol):
        if state == '0':
            if symbol == ':':
                return Tokens_Enum.COLON
            if symbol == ';':
                return Tokens_Enum.SEMICOLON
            if symbol == '.':
                return Tokens_Enum.DOT
            if symbol == ',':
                return Tokens_Enum.COMMA
            if symbol == '(':
                return Tokens_Enum.OPEN_PARENTHESIS
            if symbol == ')':
                return Tokens_Enum.CLOSE_PARENTHESIS
            if symbol == '[':
                return Tokens_Enum.OPEN_BRACKET
            if symbol == ']':
                return Tokens_Enum.CLOSE_BRACKET
            if symbol == '{':
                return Tokens_Enum.OPEN_CURLY_BRACKET
            if symbol == '}':
                return Tokens_Enum.CLOSE_CURLY_BRACKET


    punctuation_accepting = [
        Tokens_Enum.COLON,
        Tokens_Enum.SEMICOLON,
        Tokens_Enum.DOT,
        Tokens_Enum.COMMA,
        Tokens_Enum.OPEN_BRACKET,
        Tokens_Enum.OPEN_PARENTHESIS,
        Tokens_Enum.CLOSE_BRACKET,
        Tokens_Enum.CLOSE_PARENTHESIS,
        Tokens_Enum.OPEN_CURLY_BRACKET,
        Tokens_Enum.CLOSE_CURLY_BRACKET
    ]

    return '0', punctuation_transition, punctuation_accepting