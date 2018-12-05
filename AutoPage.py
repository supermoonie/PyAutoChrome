from abc import ABC, abstractmethod


class AutoPage(ABC):

    def navigate_until_dom_ready(self, url, timeout):
        pass

    @abstractmethod
    def get_this(self):
        pass

