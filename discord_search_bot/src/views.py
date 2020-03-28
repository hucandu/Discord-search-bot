import discord
from .helpers import SearchBotHelpers
from .services import scrape_service


class SearchBotConnectionView(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        search_bot_helper = SearchBotHelpers(message.content)
        is_trigger_message = search_bot_helper.check_if_trigger_message()
        if is_trigger_message:
            search_text = search_bot_helper.get_search_item()
            links = scrape_service.google_search_scrape(search_text)
            embed = search_bot_helper.create_search_embed(discord,links)
            await message.channel.send(embed=embed)
