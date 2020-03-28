from django.conf import settings
from discord_search_bot.src.views import SearchBotConnectionView
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "starts websocket connection to discord to send and recieve events"

    def handle(self, *args, **options):
        search_bot_connection_view = SearchBotConnectionView()
        search_bot_connection_view.run(settings.DISCORD_TOKEN)
