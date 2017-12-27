from .abstract_acceptor import AbstractAcceptor

class FiniteStateMachine:
    def __init__(self, start_state, transition_func, accepting_states):
        self.transition_func = transition_func
        self._accepting_states = set(accepting_states)
        self._current_state = start_state

    @property
    def current_state(self):
        return self._current_state

    def move_next(self, symbol):
        self._current_state = self.transition_func(self._current_state, symbol)
        return self._current_state

    def isAccepted(self):
        return self._current_state in self._accepting_states

    def accept(self, input_string):
        for symbol in input_string:
            move_succeed = self.move_next(symbol)
            if not move_succeed:
                return False
        return self.isAccepted()


