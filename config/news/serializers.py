from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    MainBlockTitle = serializers.CharField(source="title")
    MainBlockUrl = serializers.CharField(source='get_absolute_url')
    MainBlock = serializers.CharField(source='launcher_image')

    class Meta:
        model = News
        fields = ['MainBlock', 'MainBlockTitle', 'MainBlockUrl']