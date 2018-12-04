

class AutoChrome(object):
    def __init__(self, chrome_process=None):
        self.chrome_process = chrome_process

    def close(self):
        if self.chrome_process is not None:
            self.chrome_process.terminate()

