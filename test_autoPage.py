import time
from unittest import TestCase

from Launcher import Launcher


class TestAutoPage(TestCase):

    def test_navigate_until_dom_ready(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)

    def test_navigate(self):
        launcher = Launcher(open_dev_tools=True)
        auto_chrome = launcher.launch()
        auto_chrome.navigate(url='https://persons.shgjj.com', referrer='https://persons.shgjj.com')

    def test_back(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        auto_chrome.back()

    def test_forward(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        auto_chrome.back()
        time.sleep(2)
        auto_chrome.forward()

    def test_reload(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        auto_chrome.reload(ignore_cache=True)

    def test_stop_loading(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate(url='http://httpbin.org/#/Status_codes/get_status__codes_')
        time.sleep(2)
        auto_chrome.stop_loading()

    def test_get_frame_id(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)
        frame_id = auto_chrome.get_frame_id(url='https://persons.shgjj.com/')
        print(frame_id)

    def test_add_script_to_evaluate_on_new_document(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.add_script_to_evaluate_on_new_document('alert(1);')
        auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
