from . serializers import ArticleSerializer
from rest_framework import generics
from articles.models import Article
from rest_framework import permissions

class ArticleListApiView(generics.ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all().filter(published=True)


class ArticleCreateApiView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)