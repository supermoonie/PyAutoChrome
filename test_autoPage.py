from unittest import TestCase
from Launcher import Launcher


class TestAutoPage(TestCase):
    def test_back(self):
        self.fail()

    def test_get_frame_id(self):
        launcher = Launcher()
        auto_chrome = launcher.launch()
        auto_chrome.navigate_until_dom_ready(url='https://persons.shgjj.com', timeout=5)
        frame_id = auto_chrome.get_frame_id(url='https://persons.shgjj.com/')
        print(frame_id)
