from django.shortcuts import render, get_object_or_404
from samp_client.client import SampClient
from .models import News, Tag


def news(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    news = News.objects.filter(is_published=True).prefetch_related('tags').order_by('-created_at')

    context = {
        'online': info.players,
        'peak_online': info.max_players,
        'news': news
    }

    return render(request, 'news/news.html', context)


def news_detail(request, slug):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    news_detail = get_object_or_404(News, slug=slug, is_published=True)
    news_detail.increment_views()

    context = {
        'online': info.players,
        'peak_online': info.max_players,
        'news_detail': news_detail
    }

    return render(request, 'news/news-detail.html', context)
