from rest_framework import generics
from rest_framework import filters

from news.models import Post
from news.serializers import NewsSerializer


class NewsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title', 'url', 'created']

