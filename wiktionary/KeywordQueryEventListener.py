from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
import logging

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):

    def get_action_to_render(self, name, description, on_enter=None):
        item = ExtensionResultItem(name=name,
                                   description=description,
                                   icon='images/icon.png',
                                   on_enter=on_enter or DoNothingAction())

        return RenderResultListAction([item])

    def on_event(self, event, extension):
        data = event.get_argument()
        language_pref = extension.preferences['language']

        logger.debug(language_pref)

        if data:
            return self.get_action_to_render(name="Search for",
                    description=data,
                    on_enter=OpenUrlAction("https://%s.wiktionary.org/wiki/%s" % (language_pref, data)))
        else:
            return self.get_action_to_render(name="Type in your query",
                                             description="Example: def hurluberlu")