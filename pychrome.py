import PyChromeDevTools as pcd
import time
from Launcher import Launcher
import requests


def wait_dom_complete(ch):
    while True:
        if ch.Runtime.evaluate(expression="document.readyState == 'complete'")['result']['result']['value']:
            return
        else:
            time.sleep(0.15)


if __name__ == '__main__':
    launcher = Launcher(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
    launcher.launch()
    # launch(path='C:/app/chrome-win/chrome.exe')
    host = '127.0.0.1'
    port = 9222
    while True:
        try:
            requests.get('http://{}:{}/json'.format(host, port))
            break
        except ConnectionError:
            time.sleep(0.5)
    chrome = pcd.ChromeInterface(host=host, port=port)
    chrome.Network.enable()
    chrome.Page.enable()
    chrome.Page.setLifecycleEventsEnabled(enabled=True)
    chrome.Security.setIgnoreCertificateErrors(ignore=True)
    navigate_result = chrome.Page.navigate(url='https://persons.shgjj.com')
    time.sleep(9)
    # wait_dom_complete(chrome)
    # chrome.Runtime.evaluate(expression='alert(1);')
