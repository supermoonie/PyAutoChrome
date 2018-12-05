import platform
from abc import ABC, abstractmethod
from enum import Enum, unique

import Conditions
import Launcher


@unique
class TransitionType(Enum):
    link = 'link',
    typed = 'typed',
    address_bar = 'address_bar',
    auto_bookmark = 'auto_bookmark',
    auto_subframe = 'auto_subframe',
    manual_subframe = 'manual_subframe',
    generated = 'generated',
    auto_toplevel = 'auto_toplevel',
    form_submit = 'form_submit',
    reload = 'reload',
    keyword = 'keyword',
    keyword_generated = 'keyword_generated',
    other = 'other'

    def __str__(self):
        return '%s' % self._value_


class AutoPage(ABC):

    def navigate_until_dom_ready(self, url, timeout):
        navigate_result = self.navigate(url=url)
        self.get_this().wait_condition(condition=Conditions.wait_dom_ready, timeout=timeout)
        return navigate_result

    def navigate(self, url):
        if url is None or url.strip() == '':
            raise ValueError('url is empty')
        that = self.get_this()
        return that.chrome.Page.navigate(url=url)

    def navigate(self, url, referrer, transition_type, frame_id):
        pass

    @abstractmethod
    def get_this(self):
        pass


if __name__ == '__main__':
    if 'Darwin' == platform.system():
        launcher = Launcher.Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    else:
        launcher = Launcher.Launcher(path='C:/app/chrome-win/chrome.exe')
    auto_chrome = launcher.launch()
    result = auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)
    print(result)
