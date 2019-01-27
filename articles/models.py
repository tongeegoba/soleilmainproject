from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Article(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    other_authors = models.CharField(max_length=300, blank=True, null=True, default='None')
    content = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    up_votes = models.IntegerField(default=0, editable=False)

    def upvote(self):

        self.up_votes += 1
        return self.up_votes

    def __str__(self):
        return self.title