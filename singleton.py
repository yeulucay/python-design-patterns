"""
# singleton pattern #
singleton pattern is a 'creational' pattern
"""

class Singleton():
    """ Singleton Class """
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super().__new__(cls, *args, **kwargs)

        return cls._singleton


if __name__ == '__main__':
    c1 = Singleton()
    c2 = Singleton()
    print(c1 == c2) #  returns True, instances are equal

