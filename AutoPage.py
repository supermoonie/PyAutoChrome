from abc import ABC, abstractmethod
from collections import deque
from enum import Enum, unique
import Event

import Conditions


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


@unique
class Behavior(Enum):
    deny = 'deny',
    allow = 'allow',
    default = 'default'

    def __str__(self):
        return '%s' % self._value_


class AutoPage(ABC):

    def navigate_until_dom_ready(self, url, timeout):
        navigate_result = self.navigate(url=url)
        self.get_this().wait_condition(condition=Conditions.wait_dom_ready, timeout=timeout)
        return navigate_result

    def navigate_until_dialog_opening(self, url, timeout):
        navigate_result = self.navigate(url=url)
        dialog_result = self.get_this().wait_event(event=Event.Events.PageJavascriptDialogOpening, timeout=timeout)
        dialog = dialog_result[0]
        return navigate_result, dialog

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

    def reload(self, ignore_cache=False, script_to_evaluate_on_load=None):
        self.get_this().chrome.Page.reload(ignoreCache=ignore_cache, scriptToEvaluateOnLoad=script_to_evaluate_on_load)

    def stop_loading(self):
        self.get_this().chrome.Page.stopLoading()

    def set_content(self, html):
        if html is None or html.strip() == '':
            raise ValueError('html is empty!')
        that = self.get_this()
        target_id = that.target_id
        target_info = that.chrome.Target.getTargetInfo(targetId=target_id)
        current_url = target_info['targetInfo']['url']
        frame_id = self.get_frame_id(current_url)
        that.chrome.Page.setDocumentContent(frameId=frame_id, html=html)

    def set_download_behavior(self, behavior=Behavior.default, download_path=None):
        that = self.get_this()
        that.chrome.Page.setDownloadBehavior(behavior=behavior.value[0], downloadPath=download_path)

    def get_frame_id(self, url):
        if url is None or url.strip() == '':
            raise ValueError('url is empty!')
        that = self.get_this()
        frame_resource_tree = that.chrome.Page.getResourceTree()['frameTree']
        trees = deque()
        trees.append(frame_resource_tree)
        while trees:
            tree = trees.pop()
            if url == tree['frame']['url']:
                return tree['frame']['id']
            if 'childFrames' in tree and tree['childFrames'] is not None and len(tree['childFrames']) > 0:
                for child_frame in tree['childFrames']:
                    trees.append(child_frame)
        return None

    def add_script_to_evaluate_on_new_document(self, source):
        if source is None or source.strip() == '':
            raise ValueError('source is empty!')
        that = self.get_this()
        return that.chrome.Page.addScriptToEvaluateOnNewDocument(source=source)

    def handle_java_script_dialog(self, accept=True, prompt_text=None):
        that = self.get_this()
        that.chrome.Page.handleJavaScriptDialog(accept=accept, promptText=prompt_text)

    def get_content(self, url):
        if url is None or url.strip == '':
            return None
        frame_id = self.get_frame_id(url=url)
        that = self.get_this()
        return that.chrome.Page.getResourceContent(frameId=frame_id, url=url)

    @abstractmethod
    def get_this(self):
        pass
