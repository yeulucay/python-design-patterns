"""
# observer pattern #
observer pattern is a 'behavioral' pattern
"""

class NewsAgency():
    """ subject class """
    def __init__(self):
        self.observers = []
        self._news = None

    def attach(self, observer):
        """ observer attachment """
        self.observers.append(observer)

    @property
    def news(self):
        """ news getter """
        return self._news

    @news.setter
    def news(self, news):
        self._news = news
        self._update_observers()  # update subscriber

    def _update_observers(self):
        """ update all subscribers """
        for observer in self.observers:
            observer()

class Subscriber():
    """ observer class """
    def __init__(self, news_agency):
        self.news_agency = news_agency

    def __call__(self):
        print(self.news_agency.news)


if __name__ == '__main__':
    na = NewsAgency()
    s = Subscriber(na)
    na.attach(s)
    na.news = "Donald Trump is 45th presiden of US"
