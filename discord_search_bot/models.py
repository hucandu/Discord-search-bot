from django.contrib.auth.models import User


class SearchHistory(models.Model):
    searched_by = models.ManyToManyField(User, on_delete=models.CASCADE)
    search_text = models.CharField(max_length=200)
    searched_at = models.DateTimeField(auto_now_add=True)

class SearchLink(models.Model):
    search_text = models.ForgeinKeyField(SearchHistory, on_delete=models.CASCADE)
    link = models.URLField()
