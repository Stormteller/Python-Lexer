import re

from .abstract_acceptor import AbstractAcceptor


class RegexAcceptor(AbstractAcceptor):
    def __init__(self, regex):
        self.pattern = re.compile(regex)

    def accept(self, input_string):
        return self.pattern.match(input_string)
