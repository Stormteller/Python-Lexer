from enum import Enum

class Tokens_Enum(Enum):
    ID = 'ID'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    MULTILINE_STRING = 'MULTILINE_STRING'
    COLON = 'COLON'
    COMMA = 'COMMA'
    DOT = 'DOT'
    SEMICOLON = 'SEMICOLON'
    INTENT_SPACE = 'INTENT_SPACE'
    IF = 'IF'
    ELSE = 'ELSE'
    ELIF = 'ELIF'
    RAISE = 'RAISE'
    EXCEPT = 'EXCEPT'
    FOR = 'FOR'
    IN = 'IN'
    WHILE = 'WHILE'
    OPEN_BRACKET = 'OPEN_BRACKET'
    OPEN_PARENTHESIS = 'OPEN_PARENTHESIS'
    CLOSE_BRACKET = 'CLOSE_BRACKET'
    CLOSE_PARENTHESIS = 'CLOSE_PARENTHESIS'
    OPEN_CURLY_BRACKET = 'OPEN_CURLY_BRACKET'
    CLOSE_CURLY_BRACKET = 'CLOSE_CURLY_BRACKET'
    CLASS = 'CLASS'
    FROM = 'FROM'
    IMPORT = 'IMPORT'
    ASSIGN = 'ASSIGN'
    GT = 'GT'
    GTE = 'GTE'
    LT = 'LT'
    LTE = 'LTE'
    EQ = 'EQ'
    NOT_EQ = 'NOT_EQ'
    NONE = 'NONE'
    RETURN = 'RETURN'
    DEF = 'DEF'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    POWER = 'POWER'
    PLUS_EQ = 'PLUS_EQ'
    MINUS_EQ = 'MINUS_EQ'
    MULTIPLY_EQ = 'MULTIPLY_EQ'
    DIVIDE_EQ = 'DIVIDE_EQ'
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
