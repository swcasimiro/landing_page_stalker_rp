from django.shortcuts import render
from samp_client.client import SampClient


def news(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()


    context = {
        'online': info.players,
        'peak_online': info.max_players,
    }

    return render(request, 'news/news.html', context)

def news_detail(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    context = {
        'online': info.players,
        'peak_online': info.max_players,
    }

    return render(request, 'news/news-detail.html', context)
