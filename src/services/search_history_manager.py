from src.models import SearchHistory,User

class SearchHistoryManager:
    def record_search_history(self, user, content):
        username = self._construct_username(user.name, user.discriminator)
        user_instance,_ = User.objects.get_or_create(username=username)
        SearchHistory.objects.create(search_text=content, searched_by=user_instance)

    def get_search_history(self, user, keyword):
        return SearchHistory.objects.filter(search_text__icontains=keyword)


    def _construct_username(self, name, discriminator):
        return "{name}#{code}".format(name=name,code=discriminator)
