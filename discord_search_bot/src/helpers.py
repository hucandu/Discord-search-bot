import random
from discord_search_bot.src.constants import (
    TRIGGER_KEYWORD,
    LINK_LIMIT,
    SEARCH_EMBED_TITLE,
    SEARCH_EMBED_DESCRIPTION,
    COLOR_CODE
)


class SearchBotHelpers:
    def __init__(self, content):
        self.content = content

    def check_if_trigger_message(self):
        return True if self.content.startswith(TRIGGER_KEYWORD) else False

    def get_search_item(self):
        return self.content.replace(TRIGGER_KEYWORD, "", 1)

    def create_search_embed(self, client_context, links):
        title = SEARCH_EMBED_TITLE
        description = SEARCH_EMBED_DESCRIPTION.format(
            limit=LINK_LIMIT, search_text=self.get_search_item()
        )
        embed = client_context.Embed(
            title=title, description=description, color=COLOR_CODE
        )
        for index in range(len(links)):
            embed.add_field(name="Link {}".format(index+1),value=links[index], inline=False)
        return embed
