"""
# strategy pattern #
strategy pattern is a 'behavioral' pattern
"""

from abc import ABC, abstractmethod

"""
this is for python 3.4+
For 3.0+ instead ABC, you should use 'class BaseStrategy(metaclass=ABCMeta)'
"""
class BaseStrategy(ABC):
    """ Base strategy abstract class """
    @abstractmethod
    def play(self):
        """ abstract method """
        pass

class DefensiveStrategy(BaseStrategy):
    """ Concrete Strategy """
    def play(self):
        """ abstract method implementation """
        print("defensive played")

class OffensiveStrategy(BaseStrategy):
    """ Concrete Strategy """
    def play(self):
        """ abstract method implementation """
        print("offensive played")


class FootballTeam(object):
    """ strategy usage """

    def set_strategy(self, value):
        self._strategy = value

    strategy = property(None, set_strategy)

    def match(self):
        """ strategy trigger """
        print("match started")
        self._strategy.play()

if __name__ == '__main__':
    team = FootballTeam()
    team.strategy = OffensiveStrategy()
    team.match()