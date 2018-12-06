

class AutoChromeException(Exception):
    def __init__(self, *args):
        self.args = args
