"""
# template pattern #
template pattern is a 'behavioral' pattern
difference between strategy: strategy run-time algorithm selection, template compile time
"""

from abc import ABC, abstractmethod

class Trip(ABC):

    """ Base Class for a Trip """
    @abstractmethod
    def visitors_arrives(self):
        pass
    
    @abstractmethod
    def visitors_placed_rooms(self):
        pass

    @abstractmethod
    def visitors_dinner(self):
        pass


class Trip1(Trip):

    def trip_summary(self):
        self.visitors_arrives()
        self.visitors_placed_rooms()
        self.visitors_dinner()

    """ Concrete class 1 """
    def visitors_arrives(self):
        print("Visitors arrived by plane")

    def visitors_placed_rooms(self):
        print("Visitors stays in 5 star rooms")

    def visitors_dinner(self):
        print("Visitors eat unlimited")

class Trip2(Trip):

    def trip_summary(self):
        self.visitors_arrives()
        self.visitors_placed_rooms()
        self.visitors_dinner()

    """ Concrete class 1 """
    def visitors_arrives(self):
        print("Visitors arrived by bus")

    def visitors_placed_rooms(self):
        print("Visitors stays in 4 star rooms")

    def visitors_dinner(self):
        print("Visitors eat self service")


if __name__ == '__main__':
    t1 = Trip1()
    t1.trip_summary()

    t2 = Trip2()
    t2.trip_summary()
    