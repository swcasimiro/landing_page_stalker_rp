from django.shortcuts import render
from samp_client.client import SampClient
from .models import Launcher, RulesProject
from news.models import News


def index(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    launcher = Launcher.objects.first()

    news = News.objects.filter(is_published=True).prefetch_related('tags').order_by('-created_at')[:5]

    context = {
        'online': info.players,
        'peak_online': info.max_players,
        'launcher': launcher,
        'news': news
    }

    return render(request,'landing_page/index.html', context)


def policy(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    context = {
        'online': info.players,
        'peak_online': info.max_players,
    }

    return render(request, 'landing_page/policy.html', context)


def rules(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    context = {
        'online': info.players,
        'peak_online': info.max_players,
    }

    return render(request, 'landing_page/rules.html', context)


def rules_project(request):
    with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
        info = client.get_server_info()
        clients = client.get_server_clients_detailed()

    rules_project = RulesProject.objects.all()

    context = {
        'online': info.players,
        'peak_online': info.max_players,
        'rules_project': rules_project
    }

    return render(request, 'landing_page/rules_project.html', context)
