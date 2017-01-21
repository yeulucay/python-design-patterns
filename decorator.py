""" decorator pattern """

import datetime

def log(func):
    """ log decorator """
    def wrapper(*args, **kwargs):
        """ wrapper function """
        print("{0} {1} function log. With args {2}"
              .format(datetime.datetime.now(), func.__name__, args))

        r_val = func(*args, **kwargs)

        return r_val

    return wrapper

@log
def test1(a, b, c):
    """ test function 1 """
    print("test1 called")

@log
def test2(x, y):
    """ test function 2 """
    print("test2 called")

# other usage of decorator pattern
# test1 = log(test1)  # decorated with log
# test2 = log(test2) # decorated with log

if __name__ == '__main__':
    test1(10,11,12)
    test2("x-val","y-val")