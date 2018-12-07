import platform
import subprocess
import tempfile
import os
import time
import requests
from AutoChrome import AutoChrome


DEFAULT_ARGS = ('--disable-translate', '--disable-extensions', '--disable-background-networking',
                '--safebrowsing-disable-auto-update', '--disable-sync', '--metrics-recording-only',
                '--disable-default-apps',
                '--mute-audio', '--no-first-run', '--no-default-browser-check', '--disable-plugin-power-saver',
                '--disable-popup-blocking', '--disable-background-timer-throttling', '--disable-breakpad',
                '--disable-dev-shm-usage', '--disable-hang-monitor', '--disable-client-side-phishing-detection',
                '--disable-ipc-flooding-protection', '--disable-prompt-on-repost',
                '--disable-renderer-backgrounding',
                '--password-store=basic', '--use-mock-keychain', '--disable-infobars', '--process-per-tab',
                'about:blank', '--remote-debugging-address=127.0.0.1')


class Launcher:

    def __init__(self, path=None, user_data_dir=None, port=9222, open_dev_tools=False, incognito=False, headless=False):
        if path is None or path.strip() == '':
            # raise ValueError('path is empty')
            if 'Darwin' == platform.system():
                    path = '/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium'
            else:
                path = 'C:/app/chrome-win/chrome.exe'
        self.path = path
        if user_data_dir is None or user_data_dir.strip() == '':
            self.user_data_dir = tempfile.gettempdir() + os.path.sep + 'py_auto_chrome'
        self.open_dev_tools = open_dev_tools
        self.port = port
        self.incognito = incognito
        self.headless = headless

    def launch(self):
        args = [self.path, '--remote-debugging-port=' + str(self.port), '--user-data-dir=' + self.user_data_dir]
        if self.open_dev_tools:
            args.append('--auto-open-devtools-for-tabs')
        if self.incognito:
            args.append('--incognito')
        if self.headless:
            pass
        args = args + list(DEFAULT_ARGS)
        p = subprocess.Popen(args=args)
        return AutoChrome(port=self.port, chrome_process=p)


if __name__ == '__main__':
    launcher = Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    auto_chrome = launcher.launch()
    while True:
        try:
            time.sleep(0.5)
            requests.get('http://127.0.0.1:9222/json')
            break
        except IOError:
            pass
    time.sleep(8)
    auto_chrome.close()
