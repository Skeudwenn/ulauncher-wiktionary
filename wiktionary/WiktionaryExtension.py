from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent
from .KeywordQueryEventListener import KeywordQueryEventListener

class WiktionaryExtension(Extension):

    def __init__(self):
        super(WiktionaryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())




       