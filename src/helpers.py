import base64
import random
from src.constants import (
    SEARCH_TRIGGER_KEYWORD,
    HISTORY_TRIGGER_KEYWORD,
    GREETINGS_TRIGGER_KEYWORD,
    LINK_LIMIT,
    SEARCH_EMBED_TITLE,
    SEARCH_EMBED_DESCRIPTION,
    SEARCH_COLOR_CODE,
    HISTORY_EMBED_TITLE,
    HISTORY_EMBED_DESCRIPTION,
    HISTORY_COLOR_CODE,
)


class SearchBotHelpers:
    """Short summary.

    All helping functions to process or format string
    or objects

    Parameters
    ----------
    content : String
        message string requested by user.


    """

    def __init__(self, content):
        self.content = content

    def get_trigger_message(self):
        """Short summary.

        extracts trigger message from requested message string

        Returns
        -------
        type string
            returns None if no trigger keyword found else trigger string

        """
        if self.content.startswith(SEARCH_TRIGGER_KEYWORD):
            return SEARCH_TRIGGER_KEYWORD
        elif self.content.startswith(HISTORY_TRIGGER_KEYWORD):
            return HISTORY_TRIGGER_KEYWORD
        elif self.content.startswith(GREETINGS_TRIGGER_KEYWORD):
            return GREETINGS_TRIGGER_KEYWORD

    def get_search_item(self):
        """Short summary.

        extracts search item space from requested message

        Returns
        -------
        type string
            return search space string

        """
        return self.content.replace(SEARCH_TRIGGER_KEYWORD, "", 1)

    def get_recent_keyword(self):
        """Short summary.

        extracts recent query item from requested message

        Returns
        -------
        type string
            return recent query string

        """
        return self.content.replace(HISTORY_TRIGGER_KEYWORD, "", 1)

    def create_search_embed(self, client_context, links):
        """Short summary.

        creates embed object with searched links

        Parameters
        ----------
        client_context : discord object
        links : list of strings

        Returns
        -------
        embed object

        """
        embed = self._embed_construct(
            client_context,
            SEARCH_EMBED_TITLE,
            SEARCH_EMBED_DESCRIPTION.format(
                limit=LINK_LIMIT, search_text=self.get_search_item()
            ),
            SEARCH_COLOR_CODE,
        )
        for index in range(len(links)):
            embed.add_field(
                name="Link {}".format(index + 1), value=links[index], inline=False
            )
        return embed

    def create_history_embed(self, client_context, search_history, keyword):
        """Short summary.

        creates embed object with history records

        Parameters
        ----------
        client_context : discord object
        search_history : SearchHistory queryset
        keyword : string

        Returns
        -------
        embed object

        """
        embed = self._embed_construct(
            client_context,
            HISTORY_EMBED_TITLE,
            HISTORY_EMBED_DESCRIPTION.format(keyword=keyword),
            HISTORY_COLOR_CODE,
        )
        for index in range(len(search_history)):
            embed.add_field(
                name="Searched at {date}".format(
                    date=str(search_history[index].searched_at)
                ),
                value=search_history[index].search_text,
                inline=False,
            )
        return embed

    def _embed_construct(self, client, title, description, color_code):
        """Short summary.

        a private function to construct embed header

        Parameters
        ----------
        client : discord object
        title : string
        description : string
        color_code : int

        Returns
        -------
        embed object

        """
        title = title
        description = description
        embed = client.Embed(title=title, description=description, color=color_code)
        return embed

    @staticmethod
    def base_64_encode(string):
        return base64.b64encode(string.encode("utf-8"))

    @staticmethod
    def base_64_decode(string):
        return base64.b64decode(e).decode("utf-8")

    @staticmethod
    def construct_username(name, discriminator):
        return "{name}#{code}".format(name=name, code=discriminator)
