from src.models import SearchHistory, User
from src.helpers import SearchBotHelpers


class SearchHistoryManager:
    def record_search_history(self, user, content):
        username = SearchBotHelpers.construct_username(user.name, user.discriminator)
        user_instance, _ = User.objects.get_or_create(
            username=SearchBotHelpers.base_64_encode(username)
        )
        SearchHistory.objects.create(search_text=content, searched_by=user_instance)

    def get_search_history(self, user, keyword):
        username = SearchBotHelpers.construct_username(user.name, user.discriminator)
        return SearchHistory.objects.filter(
            search_text__icontains=keyword,
            searched_by__username=SearchBotHelpers.base_64_encode(username),
        )
