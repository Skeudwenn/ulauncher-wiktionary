from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
import logging
import urllib2

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):

    def get_action_to_render(self, name, description, on_enter=None):
        return ExtensionResultItem(name=name,
                                   description=description,
                                   icon='images/icon.png',
                                   on_enter=on_enter or DoNothingAction())

    def on_event(self, event, extension):
        data = event.get_argument()
        language_pref = extension.preferences['language']

        searched_string = data.replace(" ", "%20")

        items=[]
        
        if data:
            response = urllib2.urlopen("http://%s.wiktionary.org/w/api.php?action=opensearch&search=%s&limit=5" % (language_pref, searched_string)).read()
            response_array = eval(response)

            if not response_array[1]:
                items.append(
                    self.get_action_to_render(
                        name="Something went terribly wrong !",
                        description="check the typo of your word maybe ?"
                    )
                )
            else:
                for i in range(0,4):
                    items.append(
                        self.get_action_to_render(
                            name=response_array[1][i],
                            description=response_array[2][i],
                            on_enter=OpenUrlAction(response_array[3][i])
                        )
                    )
        else:
            items.append(
                self.get_action_to_render(
                    name="Type in your query",
                    description="Example: def hurluberlu")
            )

        return RenderResultListAction(items)