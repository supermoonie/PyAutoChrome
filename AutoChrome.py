import time
import platform

import Event
import Launcher
import PyChromeDevTools
from AutoPage import AutoPage

MIN_TIMEOUT = 0.15


class AutoChrome(AutoPage):
    def __init__(self, port=9222, chrome_process=None):
        self.port = port
        self.chrome_process = chrome_process
        self.chrome = PyChromeDevTools.ChromeInterface(port=self.port, auto_connect=False)
        while True:
            try:
                time.sleep(0.05)
                self.chrome.get_tabs()
                break
            except IOError:
                pass
        for index, tab in enumerate(self.chrome.tabs):
            if 'page' == tab['type'] and 'about:blank' == tab['url']:
                self.target_id = tab['id']
                self.chrome.connect(tab=index, update_tabs=False)
                self.chrome.Page.enable()
                self.chrome.Network.enable()
                self.chrome.Page.setLifecycleEventsEnabled(enabled=True)
                return

    def get_this(self):
        return self

    def wait_condition(self, condition, timeout):
        return self.wait_conditions(conditions=[condition], timeout=timeout)

    def wait_conditions(self, conditions, timeout):
        if conditions is None:
            raise ValueError('conditions is None!')
        if type(conditions) is not list:
            raise ValueError('conditions expect list!')
        if len(conditions) == 0:
            raise ValueError("conditions length is zero!")
        if timeout is None:
            raise ValueError('timeout is None!')
        if timeout < MIN_TIMEOUT:
            raise ValueError('timeout less than ' + str(MIN_TIMEOUT) + ' s')
        start = time.time()
        while True:
            time.sleep(MIN_TIMEOUT)
            for condition in conditions:
                result = condition(self.chrome)
                if result is not None:
                    return result
            if time.time() - start >= timeout:
                raise TimeoutError

    def wait_event(self, event, timeout):
        if event is None:
            raise ValueError('event is None!')
        if type(event) is not Event.Events:
            raise ValueError('event not in Events!')
        if timeout is None:
            raise ValueError('timeout is None!')
        if timeout < MIN_TIMEOUT:
            raise ValueError('timeout less than ' + str(MIN_TIMEOUT) + ' s')
        return self.chrome.wait_event(str(event), timeout)

    def wait_lifecycle_event(self, event, timeout):
        if event is None:
            raise ValueError('event is None!')
        if type(event) is not Event.LifecycleEvents:
            raise ValueError('event not in LifecycleEvents!')
        if timeout is None:
            raise ValueError('timeout is None!')
        if timeout < MIN_TIMEOUT:
            raise ValueError('timeout less than ' + str(MIN_TIMEOUT) + ' s')
        start = time.time()
        while True:
            lifecycle_event = self.chrome.wait_event(str(Event.Events.PageLifecycleEvent))[0]
            if str(event) == lifecycle_event['params']['name']:
                return lifecycle_event
            if time.time() - start >= timeout:
                raise TimeoutError

    def close(self):
        try:
            self.chrome.Target.closeTarget(targetId=self.target_id)
            self.chrome.close()
        except IOError:
            if self.chrome_process is not None:
                self.chrome_process.terminate()


if __name__ == '__main__':
    if 'Darwin' == platform.system():
        launcher = Launcher.Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    else:
        launcher = Launcher.Launcher(path='C:/app/chrome-win/chrome.exe')
    auto_chrome = launcher.launch()
    auto_chrome.chrome.Page.navigate(url='https://persons.shgjj.com')
    # auto_chrome.wait_condition(condition=Conditions.wait_dom_ready, timeout=18)
    # result = auto_chrome.wait_event(event=Event.Events.PageFrameStoppedLoading, timeout=10)
    auto_chrome.wait_lifecycle_event(event=Event.LifecycleEvents.FirstMeaningfulPaint, timeout=15)
