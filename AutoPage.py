import platform
from abc import ABC, abstractmethod
from enum import Enum, unique

import Conditions
import Launcher
import time


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

    def navigate(self, url, referrer=None, transition_type=None, frame_id=None):
        if url is None or url.strip() == '':
            raise ValueError('url is empty!')
        that = self.get_this()
        return that.chrome.Page.navigate(url=url, referrer=referrer, transitionType=transition_type, frameId=frame_id)

    def back(self):
        that = self.get_this()
        navigation_history = that.chrome.Page.getNavigationHistory()
        index = navigation_history['currentIndex'] - 1
        if index < 0 or index >= len(navigation_history['entries']):
            return
        entry = navigation_history['entries'][index]
        if entry is not None:
            that.chrome.Page.navigateToHistoryEntry(entryId=entry['id'])

    def forward(self):
        that = self.get_this()
        navigation_history = that.chrome.Page.getNavigationHistory()
        index = navigation_history['currentIndex'] + 1
        if index >= len(navigation_history['entries']):
            return
        entry = navigation_history['entries'][index]
        if entry is not None:
            that.chrome.Page.navigateToHistoryEntry(entryId=entry['id'])

    def add_script_to_evaluate_on_new_document(self, source):
        if source is None or source.strip() == '':
            raise ValueError('source is empty!')
        that = self.get_this()
        return that.chrome.Page.addScriptToEvaluateOnNewDocument(source=source)

    @abstractmethod
    def get_this(self):
        pass


if __name__ == '__main__':
    if 'Darwin' == platform.system():
        launcher = Launcher.Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    else:
        launcher = Launcher.Launcher(path='C:/app/chrome-win/chrome.exe')
    auto_chrome = launcher.launch()
    # script_identifier = auto_chrome.add_script_to_evaluate_on_new_document('alert(1)')
    # print(script_identifier)
    result = auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
    print(result)
    # history = auto_chrome.chrome.Page.getNavigationHistory()
    # print(history)
    auto_chrome.back()
    time.sleep(2)
    auto_chrome.forward()
