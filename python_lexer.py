import re

import FA

from acceptors.finite_state_machine import FiniteStateMachine
from tokens.tokens_enum import Tokens_Enum
from tokens.token import Token


class PythonLexer:
    @staticmethod
    def get_all_acceptors():
        return [
            FiniteStateMachine(*FA.init_punctuation_FA()),
            FiniteStateMachine(*FA.init_relop_FA()),
            FiniteStateMachine(*FA.init_intent_FA()),
            FiniteStateMachine(*FA.init_number_FA()),
            FiniteStateMachine(*FA.init_string_FA()),
            FiniteStateMachine(*FA.init_multiline_string_FA()),
            FiniteStateMachine(*FA.init_operation_FA()),
            FiniteStateMachine(*FA.init_id_FA()),

            FiniteStateMachine(*FA.init_key_word_FA('class', Tokens_Enum.CLASS)),
            FiniteStateMachine(*FA.init_key_word_FA('from', Tokens_Enum.FROM)),
            FiniteStateMachine(*FA.init_key_word_FA('import', Tokens_Enum.IMPORT)),
            FiniteStateMachine(*FA.init_key_word_FA('while', Tokens_Enum.WHILE)),
            FiniteStateMachine(*FA.init_key_word_FA('for', Tokens_Enum.FOR)),
            FiniteStateMachine(*FA.init_key_word_FA('in', Tokens_Enum.IN)),
            FiniteStateMachine(*FA.init_key_word_FA('if', Tokens_Enum.IF)),
            FiniteStateMachine(*FA.init_key_word_FA('else', Tokens_Enum.ELSE)),
            FiniteStateMachine(*FA.init_key_word_FA('elif', Tokens_Enum.ELIF)),
            FiniteStateMachine(*FA.init_key_word_FA('raise', Tokens_Enum.RAISE)),
            FiniteStateMachine(*FA.init_key_word_FA('except', Tokens_Enum.EXCEPT)),
            FiniteStateMachine(*FA.init_key_word_FA('None', Tokens_Enum.NONE)),
            FiniteStateMachine(*FA.init_key_word_FA('return', Tokens_Enum.RETURN)),
            FiniteStateMachine(*FA.init_key_word_FA('def', Tokens_Enum.DEF)),
            FiniteStateMachine(*FA.init_key_word_FA('and', Tokens_Enum.AND)),
            FiniteStateMachine(*FA.init_key_word_FA('or', Tokens_Enum.OR)),
            FiniteStateMachine(*FA.init_key_word_FA('not', Tokens_Enum.NOT)),
        ]

    def tokenize(self, code):
        tokens = []
        last_token = None
        curr_token_pos_start = 0
        acceptors = PythonLexer.get_all_acceptors()
        pos = 0
        while pos < len(code):
            while acceptors:
                next_acceptors = []
                for acceptor in acceptors:
                    if acceptor.move_next(code[pos]):
                        if acceptor.isAccepted():
                            token_type = acceptor.current_state
                            if token_type not in FA.STATE_WITH_LOOK_AHEAD:
                                token_value = code[curr_token_pos_start:pos+1]
                            else:
                                token_value = code[curr_token_pos_start:pos]
                            last_token = Token(token_type, token_value)
                        else:
                            next_acceptors.append(acceptor)
                acceptors = next_acceptors
                if acceptors:
                    pos += 1
                    if pos == len(code):
                        if not acceptors[0].isAccepted():
                            last_token = None
                        break
            if last_token:
                if last_token.type not in FA.STATE_WITH_LOOK_AHEAD:
                    pos += 1
                tokens.append(last_token)
                last_token = None
                acceptors = PythonLexer.get_all_acceptors()
                curr_token_pos_start = pos
            elif pos < len(code) and (code[pos] == ' ' or code[pos-1] == '\n'):
                pos += 1
                last_token = None
                acceptors = PythonLexer.get_all_acceptors()
                curr_token_pos_start = pos
            else:
                if re.fullmatch('^[\'\"].*\n$', code[curr_token_pos_start:pos+1], flags=re.MULTILINE):
                    raise ValueError('''Tokens: {0}
                    \nUnclosed string start from {1} \n Value: {2}'''.format(tokens, curr_token_pos_start,
                                                                                   code[curr_token_pos_start:pos]))
                elif re.fullmatch('^[(\'\'\')(\"\"\")](.|\n)*$', code[curr_token_pos_start:pos+1], flags=re.MULTILINE):
                    raise ValueError('''Tokens: {0}
                    \nUnclosed multiline string start from {1} \n Value: {2}'''.format(tokens, curr_token_pos_start,
                                                                                code[curr_token_pos_start:pos]))
                else:
                    raise ValueError('''Tokens: {0}
                    \nUnexpected ID start from {1} \n Value: {2}'''.format(tokens, curr_token_pos_start,
                                                                                          code[curr_token_pos_start:pos]))


        return tokens
