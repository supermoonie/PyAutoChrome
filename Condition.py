from abc import abstractmethod

from AutoChrome import AutoChrome


class Condition(object):
    @abstractmethod
    def apply(self, auto_chrome):
        pass

