from abc import ABCMeta, abstractmethod

class AbstractAcceptor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, input_string):
        pass