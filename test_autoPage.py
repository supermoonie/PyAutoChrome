import time
from unittest import TestCase

from Launcher import Launcher
from AutoPage import Behavior
import Tools


class TestAutoPage(TestCase):

    def setUp(self):
        launcher = Launcher(open_dev_tools=False)
        self.auto_chrome = launcher.launch()

    def test_navigate_until_dom_ready(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)

    def test_navigate_until_dialog_opening(self):
        url = 'https://gzgjj.gov.cn/wsywgr/'
        navigate_result = self.auto_chrome.navigate_until_dialog_opening(url=url, timeout=5)
        print(navigate_result)
        Tools.show_info('close')

    def test_handle_java_script_dialog(self):
        url = 'https://gzgjj.gov.cn/wsywgr/'
        navigate_result = self.auto_chrome.navigate_until_dialog_opening(url=url, timeout=5)
        print(navigate_result)
        self.auto_chrome.handle_java_script_dialog(accept=True)
        Tools.show_info('close')

    def test_navigate(self):
        result = self.auto_chrome.navigate(url='https://persons.shgjj.com', referrer='https://persons.shgjj.com')
        print(result)

    def test_back(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        self.auto_chrome.back()

    def test_forward(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        self.auto_chrome.back()
        time.sleep(2)
        self.auto_chrome.forward()

    def test_reload(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)
        time.sleep(2)
        self.auto_chrome.reload(ignore_cache=True)

    def test_stop_loading(self):
        self.auto_chrome.navigate(url='http://httpbin.org/#/Status_codes/get_status__codes_')
        time.sleep(2)
        self.auto_chrome.stop_loading()

    def test_set_content(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)
        self.auto_chrome.set_content('<h1>Hello AutoChrome!<h1>')

    def test_set_download_behavior(self):
        self.auto_chrome.set_download_behavior(behavior=Behavior.deny)
        self.auto_chrome.navigate_until_dom_ready(url='https://im.qq.com/pcqq/', timeout=5)
        Tools.show_info('close')

    def test_get_frame_id(self):
        self.auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)
        frame_id = self.auto_chrome.get_frame_id(url='https://persons.shgjj.com/')
        print(frame_id)

    def test_add_script_to_evaluate_on_new_document(self):
        self.auto_chrome.add_script_to_evaluate_on_new_document('alert(1);')
        self.auto_chrome.navigate_until_dom_ready(url='https://www.baidu.com', timeout=5)

    def test_get_content(self):
        self.auto_chrome.navigate_until_dom_ready(url='http://httpbin.org/get', timeout=5)
        result = self.auto_chrome.get_content('http://httpbin.org/get')
        print(result['content'])
