from abc import ABC, abstractmethod

class AutoWindow(ABC):

    def get_current_window_id(self):
        that = self.get_this()
        result = that.chrome.Browser.getWindowForTarget(targetId=that.target_id)
        return result.get('windowId')

    def get_window_bounds(self):
        that = self.get_this()
        window_id = self.get_current_window_id()
        return that.chrome.Browser.getWindowBounds(windowId=window_id)

    def set_window_bounds(self, left=0, top=0, width=1200, height=800, windowState='normal'):
        params = locals()
        params.pop('self')
        that = self.get_this()
        window_id = self.get_current_window_id()
        return that.chrome.Browser.setWindowBounds(windowId=window_id, bounds=params)

    def set_window_state(self, window_state='normal'):
        params = {"windowState": window_state}
        that = self.get_this()
        window_id = self.get_current_window_id()
        return that.chrome.Browser.setWindowBounds(windowId=window_id, bounds=params)

    @abstractmethod
    def get_this(self):
        pass