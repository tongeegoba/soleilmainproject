from rest_framework import serializers
from articles.models import Article
from accounts.api.serializers import UserDisplaySerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'other_authors',
            'content',
            'date_created',
            'up_votes',
            'date_display'
        ]

    def get_date_display(self, obj):
        return obj.date_created.strftime("%b %d %I:%M %p")