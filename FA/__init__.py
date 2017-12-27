from .id import init_id_FA
from .intent import init_intent_FA
from .number import init_number_FA
from .operation import init_operation_FA
from .punctuation import init_punctuation_FA
from .relop import init_relop_FA
from .key_word import init_key_word_FA
from .string import init_string_FA
from .multiline_string import init_multiline_string_FA

from tokens.tokens_enum import Tokens_Enum

STATE_WITH_LOOK_AHEAD = { Tokens_Enum.PLUS, Tokens_Enum.MINUS, Tokens_Enum.MULTIPLY, Tokens_Enum.DIVIDE,
                         Tokens_Enum.ID, Tokens_Enum.INTENT_SPACE, Tokens_Enum.NUMBER, Tokens_Enum.LT, Tokens_Enum.GT,
                         Tokens_Enum.ASSIGN, Tokens_Enum.CLASS, Tokens_Enum.FROM, Tokens_Enum.IMPORT, Tokens_Enum.WHILE,
                         Tokens_Enum.FOR, Tokens_Enum.IN, Tokens_Enum.IF, Tokens_Enum.ELSE, Tokens_Enum.ELIF,
                         Tokens_Enum.RAISE, Tokens_Enum.EXCEPT, Tokens_Enum.NONE, Tokens_Enum.RETURN, Tokens_Enum.DEF,
                         Tokens_Enum.AND, Tokens_Enum.OR, Tokens_Enum.NOT }
