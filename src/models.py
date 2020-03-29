from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    searched_by = models.ForeignKey(User, on_delete=models.CASCADE)
    search_text = models.CharField(max_length=2000)
    searched_at = models.DateTimeField(auto_now_add=True)
