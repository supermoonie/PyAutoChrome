from enum import Enum, unique


@unique
class Event(Enum):
    TargetTargetCreated = 'Target.targetCreated',
    DatabaseAddDatabase = 'Database.addDatabase',
    NetworkRequestWillBeSent = 'Network.requestWillBeSent',
    NetworkResponseReceived = 'Network.responseReceived',
    NetworkLoadingFailed = 'Network.loadingFailed',
    NetworkLoadingFinished = 'Network.loadingFinished',
    PageFrameStartedLoading = 'Page.frameStartedLoading',
    PageFrameStoppedLoading = 'Page.frameStoppedLoading',
    PageJavascriptDialogOpening = 'Page.javascriptDialogOpening',
    PageJavascriptDialogClosed = 'Page.javascriptDialogClosed',
    PageLifecycleEvent = 'Page.lifecycleEvent'

    def __str__(self):
        return '%s' % self._value_


if __name__ == '__main__':
    print(str(Event.TargetTargetCreated))
