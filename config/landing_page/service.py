from samp_client.client import SampClient

with SampClient(address='sa.gambit-rp.ru', port=7777) as client:
    info = client.get_server_info()
    clients = client.get_server_clients_detailed()

print(f'Онлайн: {info.players}/{info.max_players}')

online = info.players
peak_online = info.max_players
