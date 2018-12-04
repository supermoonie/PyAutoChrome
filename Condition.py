from abc import abstractmethod


class Condition(object):
    @abstractmethod
    def apply(self, auto_chrome):
        pass

