import abc

class BaseAttack(abc.ABC):
    @abc.abstractmethod
    def generate(self, x, y):
        pass