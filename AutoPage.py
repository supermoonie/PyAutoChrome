import platform
from abc import ABC, abstractmethod

import Conditions
import Launcher

MIN_TIMEOUT = 0.15


class AutoPage(ABC):

    def navigate_until_dom_ready(self, url, timeout):
        if url is None or url.strip() == '':
            raise ValueError('url is empty')
        if timeout is None:
            raise ValueError('timeout is None!')
        if timeout < MIN_TIMEOUT:
            raise ValueError('timeout less than ' + str(MIN_TIMEOUT) + ' s')
        that = self.get_this()
        that.chrome.Page.navigate(url=url)
        return that.wait_condition(condition=Conditions.wait_dom_ready, timeout=timeout)

    @abstractmethod
    def get_this(self):
        pass


if __name__ == '__main__':
    if 'Darwin' == platform.system():
        launcher = Launcher.Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    else:
        launcher = Launcher.Launcher(path='C:/app/chrome-win/chrome.exe')
    auto_chrome = launcher.launch()
    auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)