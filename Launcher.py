import subprocess
import tempfile
import os
import time


DEFAULT_ARGS = ('--disable-translate', '--disable-extensions', '--disable-background-networking',
                '--safebrowsing-disable-auto-update', '--disable-sync', '--metrics-recording-only',
                '--disable-default-apps',
                '--mute-audio', '--no-first-run', '--no-default-browser-check', '--disable-plugin-power-saver',
                '--disable-popup-blocking', '--disable-background-timer-throttling', '--disable-breakpad',
                '--disable-dev-shm-usage', '--disable-hang-monitor', '--disable-client-side-phishing-detection',
                '--disable-ipc-flooding-protection', '--disable-prompt-on-repost',
                '--disable-renderer-backgrounding',
                '--password-store=basic', '--use-mock-keychain', '--disable-infobars', '--process-per-tab',
                'about:blank')


class Launcher:

    def __init__(self, path, user_data_dir=None, port=9222, open_dev_tools=False, incognito=False, headless=False):
        if path is None or path.strip() == '':
            raise ValueError('path is empty')
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
        return subprocess.Popen(args=args)


if __name__ == '__main__':
    launcher = Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    p = launcher.launch()
    time.sleep(8)
    p.terminate()
