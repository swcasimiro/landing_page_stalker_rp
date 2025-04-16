from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()[:1]
    serializer_class = NewsSerializer
    http_method_names = ['get']

