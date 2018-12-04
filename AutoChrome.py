import time


MIN_TIMEOUT = 0.15


class AutoChrome(object):
    def __init__(self, chrome_process=None):
        self.chrome_process = chrome_process

    def wait_for(self, condition, timeout):
        if condition is None:
            raise ValueError('condition is None!')
        if timeout is None:
            raise ValueError('timeout is None!')
        if timeout < MIN_TIMEOUT:
            raise ValueError('timeout less than ' + str(MIN_TIMEOUT) + ' s')
        start = time.time_ns()


    def close(self):
        if self.chrome_process is not None:
            self.chrome_process.terminate()
