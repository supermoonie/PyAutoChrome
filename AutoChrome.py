import time

import Conditions
import Launcher
import PyChromeDevTools

MIN_TIMEOUT = 0.15


class AutoChrome(object):
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
                self.chrome.connect(tab=index, update_tabs=False)
                return

    def wait_for(self, conditions, timeout):
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

    def close(self):
        if self.chrome_process is not None:
            self.chrome_process.terminate()


if __name__ == '__main__':
    launcher = Launcher.Launcher(path='C:/app/chrome-win/chrome.exe')
    auto_chrome = launcher.launch()
    auto_chrome.chrome.Page.navigate(url='http://httpbin.org/get')
    auto_chrome.wait_for(conditions=[Conditions.wait_dom_ready], timeout=8)
