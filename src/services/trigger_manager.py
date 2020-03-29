import discord
from src.helpers import SearchBotHelpers
from src.services import scrape_service
from src.services.search_history_manager import SearchHistoryManager
from src.constants import (
    SEARCH_TRIGGER_KEYWORD,
    HISTORY_TRIGGER_KEYWORD,
    GREETINGS_TRIGGER_KEYWORD,
    GREETINGS_REPLY,
)


class TriggerManager:
    """Short summary.

    This manager deals with the operations to trigger on requsted
    message content.

    Parameters
    ----------
    message : Discord message object
        this holds the context of message object
        comming from discord websocket

    Attributes
    ----------
    search_bot_helper : SearchBotHelper instance
    search_history_manager : SearchHistoryManager instance
    map_trigger_to_operation : a dictionary that maps the requested
    operation toavailable operation

    """

    def __init__(self, message):
        self.message = message
        self.search_bot_helper = SearchBotHelpers(message.content)
        self.search_history_manager = SearchHistoryManager()

    def perform_operation(self):
        """Short summary.

        This function identifies the requested operation trigger and
        performs that operation accordingly

        Returns
        -------
        tuple
            returns tuple containing reply string and embed object if
            operation found else returns None,None

        """
        trigger_keyword = self.search_bot_helper.get_trigger_message()
        if trigger_keyword in self.map_trigger_to_operation:
            return self.map_trigger_to_operation[trigger_keyword](self)
        else:
            return None, None

    def _search_operation(self):
        """Short summary.

        This is an operation to run the google search and scrape the
        links out of google search and construct embed object with it

        Returns
        -------
        tuple
            returns None for reply and embed object

        """
        search_text = self.search_bot_helper.get_search_item()
        self.search_bot_helper.check_validation(search_text)
        links = scrape_service.google_search_scrape(search_text)
        embed = self.search_bot_helper.create_search_embed(discord, links)
        self.search_history_manager.record_search_history(
            self.message.author, search_text
        )
        return None, embed

    def _history_operation(self):
        """Short summary.

        This is an operation to go thru database and return recent
        searches related to the query by user in embed object

        Returns
        -------
        tuple
            returns None for reply and embed object

        """
        recent_keyword = self.search_bot_helper.get_recent_keyword()
        self.search_bot_helper.check_validation(recent_keyword)
        search_history = self.search_history_manager.get_search_history(
            self.message.author, recent_keyword
        )
        embed = self.search_bot_helper.create_history_embed(
            discord, search_history, recent_keyword
        )
        return None, embed

    def _greetings_operation(self):
        """Short summary.

        This is an operation to reply simple greetings.

        Returns
        -------
        tuple
            returns greetings for reply and None embed object

        """
        return GREETINGS_REPLY, None

    map_trigger_to_operation = {
        SEARCH_TRIGGER_KEYWORD: _search_operation,
        HISTORY_TRIGGER_KEYWORD: _history_operation,
        GREETINGS_TRIGGER_KEYWORD: _greetings_operation,
    }
