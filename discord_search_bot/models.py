from django.contrib.auth.models import User


class SearchHistory(models.Model):
    chat_user = models.ForgeinKeyField(User, on_delete=models.CASCADE)
    search_keyword = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class SearchLink(models.Model):
    link_keyword = models.ForgeinKeyField(SearchHistory, on_delete=models.CASCADE)
    link_subtext = models.TextField()
    link = models.URLField()
