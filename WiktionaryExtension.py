from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class WiktionaryExtension(Extension):

    def __init__(self):
        super(WiktionaryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_argument()

        
        items = [
            ExtensionResultItem(
                icon='images/icon.png',
                name=data,
                description='Search for %s' % data,
                on_enter=OpenUrlAction("https://fr.wiktionary.org/wiki/%s" % data)
            )
        ]

        return RenderResultListAction(items)